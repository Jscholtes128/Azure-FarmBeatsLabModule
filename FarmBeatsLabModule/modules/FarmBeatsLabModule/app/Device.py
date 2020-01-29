import json
from Sensor import Sensor

class Device(object):

    def __init__(self,id,timestamp,version,sensors):
        self.id = id
        self.timestamp = timestamp
        self.version = version
        self.sensors = sensors

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)