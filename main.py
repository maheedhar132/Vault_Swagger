import json
from fastapi import FastAPI
import requests
import json


app = FastAPI()

@app.get('/request')
def getSecret(env,user):
    url = "https://43.205.145.44:8200/v1/"+env.lower()+"/data/app?version=1"

    payload={}
    headers = {
    'Authorization': 'Bearer hvs.5IPdvoTPA9zOSI2UYoaXgewp'
    }

    response = requests.request("GET", url, headers=headers, data=payload,verify=False)
    jsonString = json.loads(response.text)
    jsonStr = jsonString["data"]["data"][user]
    return jsonStr
