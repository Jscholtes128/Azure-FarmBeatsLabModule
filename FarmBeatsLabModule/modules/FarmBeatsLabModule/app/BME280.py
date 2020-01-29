import board
import busio
import adafruit_bme280
import datetime
import json
import Sensor

class BME280(object):
    
     def __init__(
            self,
            verbose = True,
            address = 0x76,
            sensor_id):

        self.verbose = verbose
        self.address = address
        self.sensor_id = sensor_id

        i2c = busio.I2C(board.SCL,board.SDA)
        bme = adafruit_bme280.Adafruit_BME280_I2C(i2c,self.address)

    def capture():
       
        sensordata = []
        timestamp = datetime.datetime.now().isoformat()
        sensordata.append({"timestamp":timestamp,"Preassure":bme280.pressure})
         
        sensor = Sensor(sensor_id,sensordata)
        
        return sensor
        print("Pressue %0.1f hPa" % bme280.pressure)

