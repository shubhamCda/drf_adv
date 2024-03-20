import json
import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

# def get_resouces(id=None):   #with/without ID
#     data = {}
#     if id is not None:
#         data = {
#             'id':id,
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,json=data)
#     print(resp.status_code)
#     print(resp.json())
    
# get_resouces(11)


def create_resource():
    new_std = {
        'name':'Dhoni',
        'rollno': 114,
        'marks': 45,
        'gf': 'Sakshi',
        'bf': 'Mahendra'
    }
    r=requests.post(BASE_URL+ENDPOINT, json=new_std)
    print(r.status_code)
    print(r.json())
create_resource()
