import board
import busio
import adafruit_bme280
import datetime
import json
from Sensor import Sensor

class BME280(object):
    
    def __init__(self,
        verbose = True,
        sensor_id="nosensorid"):

        self.verbose = verbose
        #self.address = address
        self.sensor_id = sensor_id       

    def capture(self):
        i2c = busio.I2C(board.SCL,board.SDA)
        bme = adafruit_bme280.Adafruit_BME280_I2C(i2c,0x76)
        sensordata = []
        timestamp = datetime.datetime.now().isoformat()
        sensordata.append({"timestamp":timestamp,"Preassure":bme.pressure})
        sensor = Sensor(self.sensor_id,sensordata)
        print("Pressue %0.1f hPa" % bme.pressure)
        return sensor