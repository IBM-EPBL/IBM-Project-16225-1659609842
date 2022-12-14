import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "yXIqwSJMW8_msu96HBxRumGLj14Q7YF7HqpUsusCqrCI"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["do","ph","co","bod","tc","na"]], "values": [[6.7, 7.5, 203, 2, 0.1, 27.0]]}]}


response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/0887a156-3ecf-4c19-9571-dfbed0bdef56/predictions?version=2022-11-11', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predict = response_scoring.json()
val = (predict['predictions'][0]['values'][0][0])
print(val)