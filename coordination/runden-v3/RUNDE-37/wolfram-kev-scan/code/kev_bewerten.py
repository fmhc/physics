"""Kev im Prozess (ohne Server): je Abschnitt alle Fragen des Katalogs in einem Durchgang (Zustand einmal, Fragen als Zeilen).

Laeuft in ~/brain-kev/kev/.venv (Unterprozess von kev_lauf.py). Nutzt kev.model/kev.api unveraendert (nur gelesen).
Speicher: Gewichte als fp16 geladen, LoRA eingerechnet (Delta in fp32 berechnet, auf fp16 gerundet); auf der GPU liegt
alles ausser der Einbettungstabelle (248320 x 1024), die bleibt auf der CPU (nur Nachschlagen), damit Kev neben dem
geladenen Ollama-Modell in ~1,8 GB freien P4000-Speicher passt. --geraet cpu rechnet dieselben Gewichte in fp32 (Paritaetsprobe).
Ergebnis: eine JSON-Zeile je Abschnitt (anhaengend; ein Folgelauf setzt fort). Zeitbudget: Abbruch vor --budget_s.
"""
import argparse, json, math, os, sys, time

T0 = time.time()
ap = argparse.ArgumentParser()
ap.add_argument("--abschnitte", required=True)
ap.add_argument("--fragen", required=True)
ap.add_argument("--aus", required=True)
ap.add_argument("--modell", default="kev-0.8b", choices=["kev-0.8b", "brain-kev-0.8b"])
ap.add_argument("--geraet", default="cuda", choices=["cuda", "cpu"])
ap.add_argument("--dtype", default="fp16", choices=["fp16", "fp32"], help="Rechengenauigkeit auf der GPU (fp32 nur fuer die Paritaetsprobe)")
ap.add_argument("--ids", default="", help="Datei mit Abschnitts-IDs (nur diese)")
ap.add_argument("--ohne", default="", help="Datei mit Abschnitts-IDs, die ausgelassen werden (blinde Stichprobe im Rauchlauf)")
ap.add_argument("--max", type=int, default=0, help="hoechstens so viele neue Abschnitte")
ap.add_argument("--budget_s", type=float, default=530.0, help="kein neuer Abschnitt nach so vielen Sekunden seit Prozessstart")
a = ap.parse_args()

sys.path.insert(0, "/home/fmh/brain-kev/kev")


def _rss_mib():
    try:
        for z in open("/proc/self/status"):
            if z.startswith("VmRSS:"): return int(z.split()[1]) // 1024
    except Exception: return None


def _cg_mib():
    try:
        cg = open("/proc/self/cgroup").read().strip().split("::")[-1]
        return int(open(f"/sys/fs/cgroup{cg}/memory.current").read()) // 2**20
    except Exception: return None


print(json.dumps({"ereignis": "prozess", "t_s": round(time.time() - T0, 2), "rss_mib": _rss_mib(), "cgroup_mib": _cg_mib()}), flush=True)
import torch
import torch.nn.functional as F
print(json.dumps({"ereignis": "torch_importiert", "t_s": round(time.time() - T0, 2), "rss_mib": _rss_mib(), "cgroup_mib": _cg_mib()}), flush=True)
from transformers import AutoModelForCausalLM
from kev.api import SystemOneRequest, to_record, to_answers
from kev.model import DecisionModel, PointerHead, load_tokenizer
from peft import PeftModel
print(json.dumps({"ereignis": "kev_importiert", "t_s": round(time.time() - T0, 2), "rss_mib": _rss_mib(), "cgroup_mib": _cg_mib()}), flush=True)

BASE = "/home/fmh/brain-kev/hf/hub/models--Qwen--Qwen3.5-0.8B-Base/snapshots/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68"
RUNS = {"kev-0.8b": "/home/fmh/brain-kev/hf/hub/models--jaredpalmer--kev-0.8b/snapshots/c917edefdfd72b3e9ba71455584700acc70595f6",
        "brain-kev-0.8b": "/home/fmh/brain-kev/runs/brain-kev-0.8b"}
torch.set_num_threads(1)


def log(**kw):
    kw["t_s"] = round(time.time() - T0, 2)
    kw["rss_mib"] = _rss_mib(); kw["cgroup_mib"] = _cg_mib()
    print(json.dumps(kw, ensure_ascii=False), flush=True)


class CPUEinbettung(torch.nn.Module):
    """Einbettung auf der CPU nachschlagen, Ergebnis auf das Rechengeraet. Gewicht in einer Liste, damit .to() es nicht verschiebt."""
    def __init__(self, w, dev, dtype):
        super().__init__()
        self._w = [w]; self._dev = dev; self._dtype = dtype

    def forward(self, ids):
        return F.embedding(ids.to("cpu"), self._w[0]).to(device=self._dev, dtype=self._dtype)


def laden():
    run = RUNS[a.modell]
    meta = torch.load(f"{run}/head.pt", map_location="cpu")
    log(ereignis="meta", base=meta.get("base"), base_revision=meta.get("base_revision"), head_dim=meta.get("head_dim"),
        option_isolation=meta.get("option_isolation", False), weights_dtype=meta.get("weights_dtype"))
    tok = load_tokenizer(BASE)
    dev = a.geraet
    dt = {"fp16": torch.float16, "fp32": torch.float32}[a.dtype]
    if dev == "cpu": dt = torch.float32
    # Eigener Lader statt DecisionModel.__init__ (gleiche Felder): Gewichte direkt auf das Rechengeraet laden (device_map),
    # damit der Host-Speicher unter MemoryMax=4G bleibt (Rauchlauf 0: 4,0 GB Spitze beim Laden ueber die CPU).
    m = DecisionModel.__new__(DecisionModel)
    torch.nn.Module.__init__(m)
    m.lm = AutoModelForCausalLM.from_pretrained(BASE, dtype=dt, attn_implementation="sdpa", device_map={"": dev}).model
    m.pad_id = tok.pad_token_id if tok.pad_token_id is not None else 0
    m.hybrid = "linear_attention" in set(getattr(m.lm.config, "layer_types", None) or [])
    m.option_isolation = meta.get("option_isolation", False)
    m.head = PointerHead(m.lm.config.hidden_size, dp=meta.get("head_dim", 256))
    m.device = dev
    log(ereignis="basis_geladen", klasse=type(m.lm).__name__, hybrid=m.hybrid,
        gpu_belegt_mib=(torch.cuda.memory_allocated() // 2**20 if dev == "cuda" else None))
    m.lm = PeftModel.from_pretrained(m.lm, run)
    m.lm = m.lm.merge_and_unload()            # Delta in fp32 berechnet, in die Basisgewichte (dt) eingerechnet
    if dev == "cuda":
        w = m.lm.embed_tokens.weight.data.to("cpu")
        m.lm.embed_tokens = CPUEinbettung(w, dev, dt)
        torch.cuda.empty_cache()
    m.head.load_state_dict(meta["head"]); m.head.to(dev); m.eval()
    return tok, m


def ids_aus(pfad):
    return set(x.strip() for x in open(pfad) if x.strip()) if pfad else set()


def main():
    fragen = json.load(open(a.fragen))
    fragen = {k: v for k, v in fragen.items() if not k.startswith("_")}
    nur, ohne = ids_aus(a.ids), ids_aus(a.ohne)
    fertig = set()
    if os.path.exists(a.aus):
        for z in open(a.aus):
            try: fertig.add(json.loads(z)["id"])
            except Exception: pass
    abschnitte = [json.loads(z) for z in open(a.abschnitte, encoding="utf-8")]
    offen = [x for x in abschnitte if x["id"] not in fertig and (not nur or x["id"] in nur) and x["id"] not in ohne]
    log(ereignis="start", modell=a.modell, geraet=a.geraet, dtype=a.dtype, abschnitte=len(abschnitte), schon_fertig=len(fertig), offen=len(offen),
        torch=torch.__version__, cuda=torch.cuda.is_available(),
        gpu=(torch.cuda.get_device_name(0) if torch.cuda.is_available() else None))
    if a.geraet == "cuda":
        frei, gesamt = torch.cuda.mem_get_info()
        log(ereignis="gpu_speicher_vor_laden", frei_mib=frei // 2**20, gesamt_mib=gesamt // 2**20)
    tok, m = laden()
    log(ereignis="geladen", ladezeit_s=round(time.time() - T0, 2),
        gpu_belegt_mib=(torch.cuda.memory_allocated() // 2**20 if a.geraet == "cuda" else None))
    n = 0; zeiten = []; nan = 0
    with open(a.aus, "a", encoding="utf-8") as out:
        for x in offen:
            if a.max and n >= a.max:
                break
            if time.time() - T0 > a.budget_s:
                log(ereignis="budget_erreicht", bewertet=n)
                break
            t = time.time()
            req = SystemOneRequest(state=x["zustand"], questions=fragen)
            rec, meta_q = to_record(req)
            enc = m.encode(tok, rec, max_state=8192, max_branch=8192)
            with torch.inference_mode():
                Ls, cache, _ = m.prefix(enc)
                ps = m._branch_rows_from_prefix(enc, cache)
            roh = [p.tolist() for p in ps]
            ist_nan = any(not math.isfinite(v) for p in roh for v in p)
            nan += ist_nan
            antworten = to_answers(roh, meta_q)
            if a.geraet == "cuda":
                torch.cuda.synchronize()
            dt_ms = round((time.time() - t) * 1000, 1)
            zeiten.append(dt_ms)
            out.write(json.dumps({"id": x["id"], "ms": dt_ms, "zustand_tokens": Ls, "tokens": len(enc["ids"]), "nan": ist_nan,
                                  "antworten": antworten, "roh": {mq["id"]: [round(v, 6) for v in p] for mq, p in zip(meta_q, roh)}},
                                 ensure_ascii=False) + "\n")
            out.flush()
            n += 1
    zs = sorted(zeiten)
    log(ereignis="ende", bewertet=n, nan=nan, ms_median=(zs[len(zs) // 2] if zs else None), ms_mittel=(round(sum(zs) / len(zs), 1) if zs else None),
        ms_max=(zs[-1] if zs else None), gpu_max_mib=(torch.cuda.max_memory_allocated() // 2**20 if a.geraet == "cuda" else None),
        noch_offen=len(offen) - n)


if __name__ == "__main__":
    main()
