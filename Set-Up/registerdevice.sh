#!/bin/sh
ENDPOINT=$0
CLIENT_ID=$1 
CLIENT_SECRET=$2
TENANT_ID=$3

curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/sensorregistration.py > sensorregistration.py

mkdir templates

curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/device.json > templates/device.json
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/devicemodel.json > templates/devicemodel.json
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/sensor.json > templates/sensor.json
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/sensormodelpressure.json > templates/sensormodelpressure.json
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/sensormodeltemp.json > templates/sensormodeltemp.json

echo "--endpoint "${ENDPOINT}"--client_id "${CLIENT_ID}" --tenent_id "${TENANT_ID}" --client_secret "${CLIENT_SECRET}""

python3 sensorregistration.py --endpoint $ENDPOINT--client_id $CLIENT_ID --tenent_id $TENANT_ID --client_secret $CLIENT_SECRET
