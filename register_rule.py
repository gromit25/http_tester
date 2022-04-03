import requests
import json

body_data = {
    'rule_nm': 'custom-5',
    'rule_cntnt': "normalsource 'val1', mean=50, std=5 | zscore | filter val1_zscore > 2 | print",
    'rule_imprt': 5,
    'rule_cmmt': '',
    'rule_writer': 'jmsohn',
}

body = json.dumps(body_data)
print(body)

url = 'http://127.0.0.1:7700/api/register_rule'
response = requests.post(url, json=body)

print(url)
print(response)
if response.status_code == 200:
    print(response.text)
