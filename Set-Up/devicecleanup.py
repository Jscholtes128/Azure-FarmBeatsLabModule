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
print(CLIENT_ID)
token_response = context.acquire_token_with_client_credentials(ENDPOINT, CLIENT_ID, CLIENT_SECRET)
#Should get an access token here
access_token = token_response.get('accessToken')

#for AKS deployment you'd need to the service key in the header as well    
headers = {'Content-Type':'application/json', 'accept': 'application/json',  'Authorization':('Bearer ' + access_token)} 

resp = requests.get(ENDPOINT +'/Sensor', headers=headers)
resp_json =json.loads(resp.text)

items = resp_json['items']

for i in items:
     
    requests.delete(ENDPOINT +'/Sensor/{}'.format(i['id']), headers=headers)
    print('/Sensor/{}'.format(i['id']))


resp = requests.get(ENDPOINT +'/SensorModel', headers=headers)

resp_json =json.loads(resp.text)

items = resp_json['items']

for i in items:
   requests.delete(ENDPOINT +'/SensorModel/{}'.format(i['id']), headers=headers)
   print('/SensorModel/{}'.format(i['id']))

resp = requests.get(ENDPOINT +'/Device', headers=headers)

resp_json =json.loads(resp.text)

items = resp_json['items']

for i in items:    
    resp= requests.delete(ENDPOINT +'/Device/{}'.format(i['id']), headers=headers)
    print('/Device/{}'.format(i['id']))
    
print(resp)
resp = requests.get(ENDPOINT +'/DeviceModel', headers=headers)

resp_json =json.loads(resp.text)

items = resp_json['items']

for i in items:
   requests.delete(ENDPOINT +'/DeviceModel/{}'.format(i['id']), headers=headers)
   print('/DeviceModel/{}'.format(i['id']))