#!/bin/bash
# Aufruf eines Kleintests auf cpu6; Log lokal nach aus/logs/<name>.log
R=/home/fmh/fmhc-physics-remote/runde19-huellen-dipol
L=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-dipol/aus/logs
name=$1; shift
ssh fmh@192.168.178.69 "cd $R && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu6 $name $*" > $L/$name.log 2>&1
echo "$(date '+%H:%M:%S') fertig $name rc=$?" >> $L/kette.txt
