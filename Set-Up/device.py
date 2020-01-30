

#pip install azure-iot-hub

from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import Twin, TwinProperties
import sys

if len(sys.argv) > 1:
    connectionStr = sys.argv
else:
    connectionStr = 'HostName=IotFarmBeatLab-28693.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=ppe0phw2vN2c1Aov6zWwrPODxb6q9BsK6YyjXWXIibA='

device_id = 'FarmBeatsLabDevice'
module_id = 'FarmBeatsLabModule'

iothub_registry_manager = IoTHubRegistryManager(connectionStr)

device_state = "enabled"
new_device = iothub_registry_manager.create_device_with_sas(device_id, "", "", device_state)
new_device = iothub_registry_manager.create_module_with_sas( device_id, module_id, "", "", "")
#iothub_registry_manager.create_module_with_sas(self, device_id, module_id, managed_by, primary_key, secondary_key)




