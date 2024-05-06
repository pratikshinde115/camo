from django.urls import path
from .views import Index ,Suport

urlpatterns = [
    path('index', Index.as_view(), name='index'),
    path('Suport' , Suport.as_view(),name = 'Suport') 
]
