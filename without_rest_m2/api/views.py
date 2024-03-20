import json
from django.shortcuts import render
from django.views.generic import View
from .utils import is_json, get_object_by_id
from .mixins import HttpResponseMixin, SerializeMixin

# Create your views here.
class StudentCRUDCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, id,  *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':"Invalid Json"}), status=400)
        p_data = json.loads(data)
        id = p_data.get('id', None)
        if id is not None:
            std = self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'Student does not exist'}), status=404)
            json_data = self.serialize([std])
            return self.render_to_http_response(json_data)
            
        