#!/bin/sh
RESOURCE_GROUP=rg-FarmBeatLab-$RANDOM
IOT_HUB=IotFarmBeatLab-$RANDOM
DEVICE_ID=FarmBeatEdgeDevice
az login
az group create --name $RESOURCE_GROUP --location "Central US"
az iot hub create --name $IOT_HUB \
   --resource-group $RESOURCE_GROUP --sku S1
az iot hub device-identity create --device-id $DEVICE_ID --hub-name $IOT_HUB --edge-enabled
CONNECTION_STR=`az iot hub device-identity show-connection-string --device-id "$DEVICE_ID" --hub-name "$IOT_HUB"
echo "$CONNECTION_STR"
#sudo sed -i 's/<ADD DEVICE CONNECTION STRING HERE/'"$CONNECTION_STR"'/g' /etc/iotedge/config.yaml
