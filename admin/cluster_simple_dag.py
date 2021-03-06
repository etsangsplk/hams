from __future__ import print_function
from hams_admin import HamsConnection, DockerContainerManager
from hams_admin.deployers import python as python_deployer
import json
import requests
from datetime import datetime
import time
import numpy as np
import signal
import sys





# Stop Hams on Ctrl-C
def signal_handler(signal, frame):
    print("Stopping Hams...")
    hams_conn = HamsConnection(DockerContainerManager())
    hams_conn.stop_all()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    hams_conn = HamsConnection(DockerContainerManager())
    hams_conn.start_hams()


    f = open("../applications/simpledag/dag_description","r")
    dag_description = f.read()
    f.close()
    
    hams_conn.connect_host("202.45.128.174", "2375")
    hams_conn.connect_host("202.45.128.175", "2375")

    hams_conn.deploy_DAG("simpledag", "test", dag_description)


