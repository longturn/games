#!/bin/sh

# echo to strip whitespace
USER=$@

PASS=`grep "^${USER}:" ~/server/ltpass | sed -e 's/^.*://'`
PASS=`echo $PASS`
echo $PASS
