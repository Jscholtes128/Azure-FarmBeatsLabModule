from Sensor import Sensor
from Device import Device
import datetime
import json

x = 5
z=3
sensordata = []
timestamp = datetime.datetime.now().isoformat()
sensors =[]
j=1
while j < z:

    y=1
    while y < x:
        sensordata.append({"timestamp":timestamp,"Preassure":10})
        y+=1
    sensors.append(Sensor('asdas',sensordata))
    j+=1

device = Device("sda",timestamp,1,sensors)

print(device.toJSON())
