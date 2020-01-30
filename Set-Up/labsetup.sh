#!/bin/sh

RESOURCE_GROUP=rg-FarmBeatLab-$RANDOM
IOT_HUB=IotFarmBeatLab-$RANDOM
az group create --name RESOURCE_GROUP --location "Central US"
az iot hub create --name IOT_HUB \
   --resource-group RESOURCE_GROUP --sku S1