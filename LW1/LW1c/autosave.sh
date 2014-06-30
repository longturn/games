#!/bin/sh

while true; do
	if pgrep freeciv-server; then
		FILE="autosave-$(date '+%d.%m.%Y-%T')"
		echo "/save $FILE" >> input
		sleep 1800
		for SAV in save/autosave-*.sav; do
			gzip "$SAV"
		done
		mv save/autosave-*.sav.gz save/autosave/
	fi
done
