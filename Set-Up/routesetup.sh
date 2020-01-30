az extension add --name azure-cli-iot-ext
IOT_HUB=IotFarmBeatLab-23335
DEVICE_ID=FarmBeatEdgeDevice
#echo "Type the year that you want to check (4 digits), followed by [ENTER]:"
#read year
az iot hub device-identity create --device-id $DEVICE_ID --hub-name $IOT_HUB --edge-enabled