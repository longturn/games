#!/bin/sh

# echo to strip whitespace
USER=$1
GAMENAME=$2

#if [ "$GAMENAME" = "LT31" ]; then
# pipo controls Mrsynical; wieder controls Vendicar; mmm2 controls Johnhx; kull controls TrashKiller
#	if [ "$USER" = "Vendicar" ]; then
#		PASS=wieder
#	fi
#	if [ "$USER" = "Sokrat" ]; then
#		PASS=wieder
#	fi
#	if [ "$USER" = "Mrsynical" ]; then
#		PASS=pipo
#	fi
#	if [ "$USER" = "Johnhx" ]; then
#		PASS=mmm2
#	fi
#	if [ "$USER" = "TrashKiller" ]; then
#		PASS=kull
#	fi
#fi

PASS=`ssh longturn@kirk.jasminek.net "echo \"SELECT delegation FROM auth_user AS u JOIN game_joined j ON (u.id = j.user_id) JOIN player_player p ON p.id = j.user_id WHERE lower(username) = lower('$USER') AND game_id = '$GAMENAME'\" | psql -t | head -n 1"`
PASS=`echo $PASS`
echo $PASS
