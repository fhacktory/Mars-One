### BEGIN INIT INFO
# Provides:          rover
# Required-Start:   bluetooth 
# Required-Stop:    bluetooth 
# Default-Start:     2 
# Default-Stop:      6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO
#!/bin/sh

# le nom du service
SERVICE_NAME=rover
# le répertoire où se trouvent les exécutables du service
SERVICE_DIRECTORY=/home/robot/
# le nom du script de démarrage du service
SERVICE_STARTUP_SCRIPT=startup.sh
# le nom du script d'arrêt du service
SERVICE_SHUTDOWN_SCRIPT=shutdown.sh
 
usage()
{
        echo "-----------------------"
        echo "Usage: $0 (stop|start|restart)"
        echo "-----------------------"
}
 
if [ -z $1 ]; then
        usage
fi
 
service_start()
{
        echo "Starting service '${SERVICE_NAME}'..."
        OWD=`pwd`
        cd ${SERVICE_DIRECTORY} 
        ./${SERVICE_STARTUP_SCRIPT}
        #${SERVICE_DIRECTORY}/${SERVICE_STARTUP_SCRIPT}
        cd $OWD
        echo "Service '${SERVICE_NAME}' started successfully"
}
 
service_stop()
{
        echo "Stopping service '${SERVICE_NAME}'..."
        OWD=`pwd`
        #cd ${SERVICE_DIRECTORY} &amp;&amp; ./${SERVICE_SHUTDOWN_SCRIPT}
        ${SERVICE_DIRECTORY}/${SERVICE_SHUTDOWN_SCRIPT}
        cd $OWD
        echo "Service '${SERVICE_NAME}' stopped"
}
 
case $1 in
        stop)
                service_stop
        ;;
        start)
                service_start
        ;;
        restart)
                service_stop
                service_start
        ;;
        *)
                usage
esac
exit 0
