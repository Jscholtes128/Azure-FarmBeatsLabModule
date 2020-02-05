#!/bin/sh
ENDPOINT=$1
CLIENT_ID=$2 
CLIENT_SECRET=$3
TENANT_ID=$4

curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/sensorregistration.py > sensorregistration.py

mkdir templates

curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/device.json > /templates/device.json
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/devicemodel.json > /templates/devicemodel.json
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/sensor.json > /templates/sensor.json
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/sensormodelpressure.json > /templates/sensormodelpressure.json
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/templates/sensormodeltemp.json > /templates/sensormodeltemp.json

python3 sensorregistration.py --endpoint $ENDPOINT--client_id $CLIENT_ID --tenent_id $CLIENT_SECRET --client_secret $TENANT_ID
