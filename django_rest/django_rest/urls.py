from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_api import views

router=routers.DefaultRouter()
# router.register('api', views.EmployeeCRUDCBV, basename='api') #if we are using modelViewset then its a optional to use
router.register('api', views.EmployeeCRUDCBV) #we can use in this way also


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  #include is a function of urllib to include the urls of another app into our project's urls
]
