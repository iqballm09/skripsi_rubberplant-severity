# Program to authenticate earth engine
import json
import ee

with open('auth_key.json') as f:
    json_data = f.read()

# Preparing values
def ee_authenticate(json_data=json_data):
    # Preparing values
    json_object = json.loads(json_data, strict=False)
    service_account = json_object['client_email']
    json_object = json.dumps(json_object)
    # Authorising the app
    credentials = ee.ServiceAccountCredentials(service_account, key_data=json_object)
    ee.Initialize(credentials)
    