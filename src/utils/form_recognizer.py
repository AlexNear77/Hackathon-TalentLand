import json
import os
from azure.core.exceptions import ResourceNotFoundError
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient 

datos = {}

def extract_id_field_value(id_card, field_name):
    try:
        print(field_name)
        print('-'*25)
        print('Field Value: {0}'.format(id_card.fields.get(field_name).value))
        print('Confidence Score: {0}'.format(id_card.fields.get(field_name).confidence))
        datos[field_name] = id_card.fields.get(field_name).value
        print()
    except AttributeError:
        print('Nothing returned')

# credentials = json.load(open("credential.json"))
# API_KEY = credentials['API_KEY']
# ENDPOINT = credentials['ENDPOINT']

API_KEY = os.getenv('API_KEY')
ENDPOINT = os.getenv('ENDPOINT')

form_recognizer_client = FormRecognizerClient(ENDPOINT, AzureKeyCredential(API_KEY))

# driver_license_url = 'https://gray-kolo-prod.cdn.arcpublishing.com/resizer/5Gp4BHAD5XTGGPRAAvXetQAu3YY=/1200x675/smart/filters:quality(85)/cloudfront-us-east-1.images.arcpublishing.com/gray/KUKKLVRFP5BKJLNLGH2NWSEPRA.jpg'
driver_license_url = 'https://imengine.prod.srp.navigacloud.com/?uuid=ED02B807-1CE5-4B2F-97F6-0EE3AB39736F&type=primary&q=72&width=1024'

poller = form_recognizer_client.begin_recognize_identity_documents_from_url(driver_license_url)
print(poller.status())
result = poller.result()
# print(result)
if poller.status() == 'succeeded':
    result = poller.result()
    print(result)
    field_names = result[0].fields.keys()
    for form in result:
        for field_name in field_names:
            extract_id_field_value(form, field_name)


print(datos)
