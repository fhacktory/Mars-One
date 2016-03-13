#!/bin/sh
#
SCREEN_SESSION=rover
SCREEN=/usr/bin/screen
GREP=/bin/grep
ECHO=/bin/echo
HCI=/bin/hciconfig
ROVER_PATH=/home/robot/
ROVER_SCREEN=`$SCREEN -ls | $GREP -E "[0-9]{1,5}\.$SCREEN_SESSION.+\(Detached\)$"`
$ECHO "# checking if bluetooth is up"
BLUE_CHECK=`$HCI | $GREP -E "UP RUNNING PSCAN"`

while [ -z "$BLUE_CHECK" ] ; do
	$ECHO "Bl not UP"
	sleep 5
	BLUE_CHECK=`$HCI | $GREP -E "UP RUNNING PSCAN"`
	$ECHO "\"$BLUE_CHECK\""
done

$ECHO "# checking if rover is currently running in a screen session..."
if [ -n "$ROVER_SCREEN" ]; then
    $ECHO "-> rover is running in a screen session:"
    $ECHO "\"$ROVER_SCREEN\""
    # kill screen session that cherrymusic runs in
    $ECHO "-> killing screen session that rover runs in..."
    $SCREEN -X -S $SCREEN_SESSION quit
else
    $ECHO "-> rover not running, good."
fi
$ECHO "-> rover start"
cd $ROVER_PATH
$SCREEN -d -m -S $SCREEN_SESSION  "./script.py"
