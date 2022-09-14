import requests
url = "https://43.205.145.44:8200/v1/kv/data/app?version=1"

payload={}
headers = {
    'Authorization': 'Bearer hvs.5IPdvoTPA9zOSI2UYoaXgewp'
    }

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
print(response.text)