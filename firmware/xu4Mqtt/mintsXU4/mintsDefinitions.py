
from getmac import get_mac_address
import serial.tools.list_ports
import yaml
import pandas as pd

dataFolder                = "/home/teamlary/mintsData/raw"
metaFolder                = "/home/teamlary/mintsData/meta"

  


credentialsFile       = 'mintsXU4/credentials.yml'

mqttBroker            = "mqtt.circ.utdallas.edu"
mqttPort              =  8883  # Secure port

credentials            = yaml.load(open(credentialsFile), Loader=yaml.Loader)

# nodeInfo               = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/id_lookup.csv')

nodeInfo               = pd.read_csv('https://raw.githubusercontent.com/mi3nts/cloudInfluxUpdates/refs/heads/main/lists/testLookUp.csv')

if __name__ == "__main__":

    print("Data Folder Raw      : {0}".format(dataFolder))
    print("Credentials File     : {0}".format(credentialsFile))


    
    #-------------------------------------------#
    print("Node Info :")
    print(nodeInfo)
