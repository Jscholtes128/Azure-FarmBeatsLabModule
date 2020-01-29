from Sensor import Sensor
from Device import Device
from BME280 import BME280
import time
import AppState

import iothub_client
from iothub_client import (IoTHubMessage)


class InputCapture(object):

    def __init__(
            self,
            verbose = True,
            interval = 6000):

        self.verbose = verbose
        self.interval = interval
        self.running = True
        bme = BME280(verbose,0x76,"13213")
    
    def stop():
        self.running = False
    
    def start():
        while(running):
            timestamp = datetime.datetime.now().isoformat()
            sensors = []
            sensors.append(bme.capture())

            device = Device("asdas",timestamp,1,sensors)

            #"deviceid": "<id of the Device created>",
            #"timestamp": "<timestamp in ISO 8601 format>",
            #"version" : "1",
            #"sensors": [

            message = IoTHubMessage(device.toJSON())
            AppState.HubManager.send_event_to_output("output1", message, 0)
            #self.lastMessageSentTime=datetime.now()

            time.sleep(interval)