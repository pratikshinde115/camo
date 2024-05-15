from django.shortcuts import render

# Create your views here.
from .serializer import HomeSerializer
from django.core.mail import send_mail
from .utils import send_thank_you_email
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render ,redirect 
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print(request.user.is_authenticated)
    return render(request, 'index.html')


@csrf_exempt
def Suport(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email =  request.POST.get('EMAIL')
        subject =  request.POST.get('subject')
        message =  request.POST.get('message')
        send_thank_you_email(email=email, name = name)

        serializer = HomeSerializer(data={'name':name,'email':email , 'subject' :subject ,'message':message })
        if serializer.is_valid():
            serializer.save()
        return redirect('index')