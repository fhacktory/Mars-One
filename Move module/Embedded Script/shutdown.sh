#!/bin/sh
#Script stop rover
SCREEN_SESSION=rover
SCREEN=/usr/bin/screen
GREP=/bin/grep
ECHO=/bin/echo
ROVER_SCREEN=`$SCREEN -ls | $GREP -E "[0-9]{1,5}\.$SCREEN_SESSION.+\(Detached\)$"`
$ECHO "# checking if rover is currently running in a screen session..."
if [ -n "$ROVER_SCREEN" ]; then
    $ECHO "-> rover is running in a screen session:"
    $ECHO "\"$ROVER_SCREEN\""
    # kill screen session that rover runs in
    $ECHO "-> killing screen session that rover runs in..."
    $SCREEN -X -S $SCREEN_SESSION quit
else
    $ECHO "-> rover not running"
fi