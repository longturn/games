Games
=====

The scripts, rulesets, configuration files and freeciv-server binaries
used for running longturn.org games.

How To Start A Game
===================
### Test Game
    set autosaves GAMEOVER
    set unitwaittime 0
    set timeout 120
    autocreate players
    start

### Real Game
    touch input
    tail -F input | sh LT37.sh
    # tail -F input | sh LT37.sh autosave-07.04.2017-13:38:46.sav

    echo '/autocreate players' >> input
    echo '/start' >> input
    echo '/syncturn 3' >> input
