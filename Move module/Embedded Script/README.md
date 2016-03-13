#README

startup.sh et shutdown.sh à placer dans le répértoire de script.py

rover.sh a placer dans /etc/init.d
Donner les droits : chmod a+x /etc/init.d/rover.sh
Exectuter au démarrage : sudo /usr/sbin/update-rc.d rover.sh defaults