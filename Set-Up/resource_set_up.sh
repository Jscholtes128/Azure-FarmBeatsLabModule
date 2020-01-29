#!/bin/sh
echo "Install Azure CLI?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) curl -L https://aka.ms/InstallAzureCli | bash; break;;
        No ) break;;
    esac
done
az login
RESOURCE_GROUP=rg-FarmBeatLab-$RANDOM
IOT_HUB=IotFarmBeatLab-$RANDOM
az group create --name RESOURCE_GROUP --location "Central US"
az iot hub create --name IOT_HUB \
   --resource-group RESOURCE_GROUP --sku S1