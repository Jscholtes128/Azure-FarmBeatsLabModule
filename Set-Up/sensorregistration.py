import requests
import json
import azure
from azure.common.credentials import ServicePrincipalCredentials
import adal

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--endpoint', help='farm beats data hub endpoint')
parser.add_argument('--client_id', help='farm beats client id')
parser.add_argument('--tenent_id', help='Azure tenent id')
parser.add_argument('--client_secret', help='farm beats client secret')

args = parser.parse_args()

print(args.endpoint)

#FarmBeats API Endpoint 
ENDPOINT = args.endpoint
CLIENT_ID = args.client_id #"<Your Client ID>"   
CLIENT_SECRET = args.client_secret#"<Your Client Secret>"   
TENANT_ID = args.tenent_id #"<Your Tenant ID>" 
AUTHORITY_HOST = 'https://login.microsoftonline.com'
AUTHORITY = AUTHORITY_HOST + '/' + TENANT_ID
#Authenticating with the credentials
context = adal.AuthenticationContext(AUTHORITY)
token_response = context.acquire_token_with_client_credentials(ENDPOINT, CLIENT_ID, CLIENT_SECRET)
#Should get an access token here
access_token = token_response.get('accessToken')


sensorlist = [{'name':'Grove Barometer Sensor (Pressure)', 'description':'Farm Beats Lab Kit Grove Barometer Sensor','modelfile':'templates/sensormodelpressure.json'},
{'name':'Grove Barometer Sensor (Temp)', 'description':'Farm Beats Lab Kit Grove Barometer Temp Sensor','modelfile':'templates/sensormodeltemp.json'}]

#for AKS deployment you'd need to the service key in the header as well    
headers = {'Content-Type':'application/json', 'accept': 'application/json',  'Authorization':('Bearer ' + access_token)} 


with open('templates/devicemodel.json') as json_file:
    devicemodel_json = json.load(json_file)

resp = requests.post(ENDPOINT +'/DeviceModel', json.dumps(devicemodel_json), headers=headers)

resp_json =json.loads(resp.text)

device_model_id = resp_json['id']

with open('templates/device.json') as json_file:
    device_json = json.load(json_file)


device_json['deviceModelId'] = device_model_id
#device_json['farmId'] = ""

resp = requests.post(ENDPOINT +'/Device', json.dumps(device_json), headers=headers)

resp_json = json.loads(resp.text)
device_id = resp_json['id']

for s in sensorlist:
    
    with open(s['modelfile']) as json_file:
        sensormodel_json = json.load(json_file)

    resp = requests.post(ENDPOINT +'/SensorModel', json.dumps(sensormodel_json), headers=headers)

    resp_json = json.loads(resp.text)
    print(resp_json)
    sensormodel_id = resp_json['id']

    with open('templates/sensor.json') as json_file:
        sensor_json = json.load(json_file)
        sensor_json['sensorModelId'] = sensormodel_id
        sensor_json['deviceId'] = device_id
        sensor_json['name'] = s['name']
        sensor_json['description'] = s['description']

    resp = requests.post(ENDPOINT +'/Sensor', json.dumps(sensor_json), headers=headers)

    resp_json = json.loads(resp.text)
    sensor_id = resp_json['id']
    print(sensor_id)

