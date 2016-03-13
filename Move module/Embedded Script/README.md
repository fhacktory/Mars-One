#README

Setup : 

put startup.sh, shutdown.sh and script.py in the same rep.

Put rover.sh in /etc/init.d
give it rights : sudo chmod a+x /etc/init.d/rover.sh
Launch at startup : sudo /usr/sbin/update-rc.d rover.sh defaults


FIX ME : script auto start at boot doesn't work (neither with update-rc nor with rc.local)
