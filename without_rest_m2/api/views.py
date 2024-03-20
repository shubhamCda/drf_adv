import json
from django.shortcuts import render
from django.views.generic import View
from .models import Student
from .utils import get_object_by_id, is_json
from .mixins import HttpResponseMixin, SerializeMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentCRUDCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, id=None, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)   #deriving from utility file (No self keyword)
        if not valid_json:
            return self.render_to_http_response(
                json.dumps({"msg": "Invalid Json"}), status=400
            )
        p_data = json.loads(data)
        id = p_data.get("id", None)
        if id is not None:
            std = get_object_by_id(id)   #No need to add self keyword  as it's a class method
            if std is None:
                return self.render_to_http_response(
                    json.dumps({"msg": "Student does not exist"}), status=404
                )
            json_data = self.serialize([std])
            return self.render_to_http_response(json_data)
        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)
