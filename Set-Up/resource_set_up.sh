#!/bin/sh
az extension add --name azure-cli-iot-ext
RESOURCE_GROUP=rg-FarmBeatLab-$RANDOM
IOT_HUB=IotFarmBeatLab-$RANDOM
STORE=farmbeatstorage$RANDOM
DEVICE_ID=FarmBeatEdgeDevice
LOCATION=centralus

az group create --name $RESOURCE_GROUP --location $LOCATION
az iot hub create --name $IOT_HUB \
   --resource-group $RESOURCE_GROUP --sku S1
az iot hub device-identity create --device-id $DEVICE_ID --hub-name $IOT_HUB --edge-enabled

sleep 30s

curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/FarmBeatsLabModule/config/deployment.arm32v7.json > deployment.arm32v7.json

az iot edge set-modules --device-id $DEVICE_ID --hub-name $IOT_HUB --content deployment.arm32v7.json

rm deployment.arm32v7.json

CONNECTION_STR_JSON=`az iot hub device-identity show-connection-string --device-id "$DEVICE_ID" --hub-name "$IOT_HUB"`
CONNECTION_STR=$(echo $CONNECTION_STR_JSON | jq '.connectionString')

echo "Connection String: ${CONNECTION_STR}"

az storage account create \
    --name $STORE \
    --resource-group $RESOURCE_GROUP \
    --location $LOCATION \
    --sku Standard_LRS 

az storage container create --account-name $STORE --name install

curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/iotedgeinstall.sh > iotedgeinstall.sh

#-i
sed  "s,[REPLACE],${CONNECTION_STR}," iotedgeinstall.sh

az storage blob upload \
    --account-name $STORE \
    --container-name install \
    --name iotedgeinstall.sh \
    --file iotedgeinstall.sh

rm iotedgeinstall.sh

end=`date -u -d "240 minutes" '+%Y-%m-%dT%H:%MZ'`
SAS=`az storage blob generate-sas --account-name "$STORE" -c install -n iotedgeinstall.sh --permissions r --expiry "$end" --https-only --full-uri`
echo "SAS: ${SAS}"

curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/geturl.py > geturl.py

python3 geturl.py --url $SAS

rm geturl.py
