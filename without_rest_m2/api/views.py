import json
from django.shortcuts import render
from django.views.generic import View
from .utils import is_json
from .mixins import HttpResponseMixin

# Create your views here.
class StudentCRUDCBV(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':"Invalid Json"}), status=400)
        p_data = json.loads(data)
        id = p_data.get('id', None)
        if id is not None:
            st
            
        