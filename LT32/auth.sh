#!/bin/sh

# echo to strip whitespace
USER=$@

if [ "$USER" = "el_perdedor" ]; then
	echo
	exit
fi

PASS=`grep "^${USER}:" ~/server/ltpass | sed -e 's/^.*://'`
PASS=`echo $PASS`
echo $PASS
