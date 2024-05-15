from django.urls import path
from .views import index ,Suport 

urlpatterns = [
    path('', index, name='index'),
    path('Suport' , Suport,name = 'Suport') ,
]
