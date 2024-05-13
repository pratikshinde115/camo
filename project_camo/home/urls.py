from django.urls import path
from .views import index ,Suport 

urlpatterns = [
    path('index', index, name='index'),
    path('Suport' , Suport.as_view(),name = 'Suport') ,
]
