import board
import busio
import adafruit_bme280
import datetime
import json
from Sensor import Sensor

class BME280(object):
    
    def __init__(self,
        verbose = True):

        self.verbose = verbose
        #self.address = address              

    def capture(self,pressure_sensor_id,temp_sensor_id):
        i2c = busio.I2C(board.SCL,board.SDA)
        bme = adafruit_bme280.Adafruit_BME280_I2C(i2c,0x76)
        sensors = []
        timestamp = datetime.datetime.now().isoformat()

        sensors.append(Sensor(pressure_sensor_id,{"timestamp":timestamp,"Pressure":bme.pressure})
        sensors.append(Sensor(temp_sensor_id,{"timestamp":timestamp,"Temperature": bme.temperature}))

        print("Pressue %0.1f hPa" % bme.pressure)
        return sensors