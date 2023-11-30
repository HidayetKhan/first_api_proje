import requests
import json
URL ='http://127.0.0.1:8000/studentapi/'

#to get data to frend end or to our client(get read function)
def get_data(id=None):
    data={}
    if id is not None:
        data ={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
    
#get_data()

#here now clinetsending the data 
def post_data():
    data={
        'name':'hidayet',
        'roll':104,
        'city':'mumbai'
    }

    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

post_data()

#to update the data
def update_data():
    data={
        'id':4,
        'name':'shaziya',
        'city':'mumbai'
    }


    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

#update_data()
#for deleting the data
def delete_data():
    data={
        'id':4
    }


    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

#delete_data()