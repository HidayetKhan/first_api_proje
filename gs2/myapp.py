#this is for third party use (how data come we seee here)
#it is clinet application means data come from client
import requests
import json
URL="http://127.0.0.1:8000/stucreate/"
data={
    'name':'anam',
    'roll':101,
    'city':'mumbai'
}

json_data=json.dumps(data)

r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)