import requests

#url = 'http://127.0.0.1:7700/api/list_rules'
url = 'http://192.168.35.66:7700/api/list_rules'
response = requests.get(url)

print(url)
print(response)
if response.status_code == 200:
    print(response.text)

print('test 입니다.')
