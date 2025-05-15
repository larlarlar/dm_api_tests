"""curl -X 'POST' \
  'http://5.63.153.31:5051/v1/account' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "login": "Thomas_Magnum",
  "email": "Thomas@Magnum.su",
  "password": "ThomasMagnumRulez"
}'"""
import pprint

import requests
"""
url = 'http://5.63.153.31:5051/v1/account'
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json'
}
json = {
    "login": "Jonathan Quayle Higgins III",
    "email": "JonathanQuayle@Higgins.IIIMagnum",
    "password": "Higgins.IIIMagnum"
}

response = requests.post(
    url=url,
    headers=headers,
    json=json
)

print(response.status_code)
# print(response.json())
"""

"""curl -X 'PUT' \
  'http://5.63.153.31:5051/v1/account/887ff689-09d5-4cbc-b443-97f67c349c90' \
  -H 'accept: text/plain'"""

url = 'http://5.63.153.31:5051/v1/account/887ff689-09d5-4cbc-b443-97f67c349c90'
headers = {
    'accept': 'text/plain'
}

response = requests.put(
    url=url,
    headers=headers
)

print(response.status_code)
pprint.pprint(response.json())
response_json=response.json()
print(response_json['resource']['rating']['quantity'])
