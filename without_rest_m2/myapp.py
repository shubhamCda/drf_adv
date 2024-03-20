import json
import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

def get_resouces(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id,
        }
    resp=requests.get(BASE_URL+ENDPOINT,json=data)
    print(resp.status_code)
    print(resp.json())
    
get_resouces()