#!/usr/bin/bash

disabled=0

while true; do
    hhkb=$(xinput list | grep "TmkBT-CCE7")
    keyboardID=$(xinput list | grep "AT" | sed 's/.*\=*\([0-9]\{2\}\).*/\1/')
    if echo $hhkb | grep -q "TmkBT"; then
        if [ $disabled == 0 ]; then
            xinput float $keyboardID
            disabled=1
        fi
    else
        if [ $disabled -eq 1 ]; then
            xinput reattach $keyboardID 3
            disabled=0
        fi
    fi
    sleep 3
done
