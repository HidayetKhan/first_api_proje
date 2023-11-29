import requests

URL="http://127.0.0.1:8000/stuinfo/2"

r=requests.get(url=URL)
data=r.json()
print(data)
#this tis not related with our project it is basically we ceated to comunicate with the apiand give the data