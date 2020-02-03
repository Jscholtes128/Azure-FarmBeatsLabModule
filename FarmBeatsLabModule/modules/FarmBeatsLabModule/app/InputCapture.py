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
            interval = 60,
            deviceID="",
            pressureSensorID="",
            tempSensorID=""):

        self.verbose = verbose
        self.interval = interval
        self.deviceID = deviceID
        self.pressureSensorID = pressureSensorID
        self.tempSensorID = tempSensorID
        self.running = True

    def __enter__(self):

        if self.verbose:
            print("inputCapture::__enter__()")
        return self
    
    def stop(self):
        self.running = False
    
    def start(self):
        bme = BME280(self.verbose)

        while(self.running):                         
            timestamp = datetime.datetime.now().isoformat()
            sensors = []
            sensors.extend(bme.capture(self.pressureSensorID,self.tempSensorID))

            device = Device(self.deviceID,timestamp,1,sensors)   
            jsn = device.toJSON()
            message = IoTHubMessage(jsn)
            print(jsn)
            AppState.HubManager.send_event_to_output("output1", message, 0)
            #self.lastMessageSentTime=datetime.now()

            time.sleep(self.interval)


    def __exit__(self, exception_type, exception_value, traceback):

        self.stop()
            