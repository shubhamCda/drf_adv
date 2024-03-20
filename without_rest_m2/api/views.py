from django.shortcuts import render
from django.views.generic import View
from .utils import is_json

# Create your views here.
class StudentCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            pass
        