import json

class Sensor(object):

    def __init__(self,id,sensorData):
        self.id = id
        self.sensorData = sensorData

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)