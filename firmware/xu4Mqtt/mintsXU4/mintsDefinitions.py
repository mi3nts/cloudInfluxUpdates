
from getmac import get_mac_address
import serial.tools.list_ports
import yaml
import pandas as pd


mintsDefinitions         = yaml.load(open("mintsXU4/mintsDefinitions.yaml"))

dataFolder         = mintsDefinitions['dataFolder']
metaFolder         = mintsDefinitions['metaFolder']


mqttBroker            = "mqtt.circ.utdallas.edu"
mqttPort              =  8883  # Secure port

credentials            = yaml.load(open('mintsXU4/credentials.yaml'), Loader=yaml.Loader)

# nodeInfo               = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/id_lookup.csv')
nodeInfo               = pd.read_csv('https://raw.githubusercontent.com/mi3nts/cloudInfluxUpdates/refs/heads/main/lists/testLookUp.csv')

if __name__ == "__main__":

    print("Data Folder Raw      : {0}".format(dataFolder))
    print("Meta Folder          : {0}".format(metaFolder))

    #-------------------------------------------#
    print("Node Info :")
    print(nodeInfo)
