import json
import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"


#GET request
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

# # Post request
# def create_resource():
#     new_std = {
#         'name':'Mangalam',
#         'rollno': 115,
#         'marks': 35,
#         'gf': 'Kirti',
#         'bf': 'Shubham'
#     }
#     r=requests.post(BASE_URL+ENDPOINT, json=new_std)
#     print(r.status_code)
#     print(r.json())
# create_resource()


#  PUT (Update Request)
def update_student():
    new_data = {
        'id':id,
        'gf': 'Sonu',
    }
    r = requests.put(BASE_URL + ENDPOINT, json=new_data)
    print(r.status_code)
    print(r.json())
update_student(1)
    