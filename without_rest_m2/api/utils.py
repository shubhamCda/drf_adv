import json

from .models import Student


def is_json(data):
    try:
        real_data =  json.loads(data)
        valid = True
    except ValueError:
        valid=False
    return valid

def get_object_by_id(self, id):
    try:
        s = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return None
    return s