import json
from django.shortcuts import render
from django.views.generic import View
from .forms import StudentForm
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
    
    def post(self,request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Please send the valid json data.'}))
        std_data = json.loads(data)
        form=StudentForm(std_data)
        if form.is_valid():
            form.save()
            return  self.render_to_http_response(json.dumps({'msg':'Resource saved successfully...'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    
    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Please enter the valid JSON data..'}))
        p_data = json.loads(data)
        id = p_data.get('id', None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'Missing argument: `id`.'}))
        std = get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({'msg': 'Invalid student ID.'}), status=404)
        
        original_data = {
            'name':std.name,
            'rollno':std.rollno,
            'marks':std.marks,
            'gf':std.gf,
            'bf':std.bf,
        }
        original_data.update(p_data)
        form=StudentForm(original_data, instance=std)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'Student updated Successfully...'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)
        
    
    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'No Data in Json format.'}))
        p_data = json.loads(data)
        id  = p_data.get("id",None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'To delete the entry ID must be required....'}))
        std = get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({"error":"Record does not exist"}),status=400)
        status, deleted_item =std.delete()
        if status==1:
            json_data = json.dumps({'msg':'Resource deleted successfully...'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'Unable to delete plz try again...'})
        return self.render_to_http_response(json_data,status=500)

