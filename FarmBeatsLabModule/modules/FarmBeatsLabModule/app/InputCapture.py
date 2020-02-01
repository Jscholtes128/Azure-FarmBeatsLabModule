from Sensor import Sensor
from Device import Device
from BME280 import BME280
import time
import AppState
import datetime
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

    def __enter__(self):

        if self.verbose:
            print("inputCapture::__enter__()")
        return self
    
    def stop(self):
        self.running = False
    
    def start(self):
        bme = BME280(self.verbose,"13213")

        while(self.running):
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

            time.sleep(self.interval)


    def __exit__(self, exception_type, exception_value, traceback):

        self.stop()
            