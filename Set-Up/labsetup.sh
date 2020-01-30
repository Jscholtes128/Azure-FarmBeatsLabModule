#!/bin/sh
RESOURCE_GROUP=rg-FarmBeatLab-$RANDOM
IOT_HUB=IotFarmBeatLab-$RANDOM
echo 's/<ADD DEVICE CONNECTION STRING HERE/'"$IOT_HUB"'/g'
az login
az group create --name $RESOURCE_GROUP --location "Central US"
az iot hub create --name $IOT_HUB \
   --resource-group $RESOURCE_GROUP --sku S1
CONNECTION_STR=`az iot hub device-identity create --device-id FarmBeatEdgeDevice --hub-name "$IOT_HUB" --edge-enabled`
sudo sed -i 's/<ADD DEVICE CONNECTION STRING HERE/'"$CONNECTION_STR"'/g' /etc/iotedge/config.yaml
