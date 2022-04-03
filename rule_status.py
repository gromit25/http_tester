import requests
import json

body_data = {
    'rule_id': 3,
}

#url = 'http://127.0.0.1:7700/api/rule_status'
url = 'http://192.168.35.66:7700/api/rule_status'
response = requests.get(url, json=body_data)

print(url)
print(response)
if response.status_code == 200:
    print(response.text)
