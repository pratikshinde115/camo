from django.contrib.auth import authenticate, login , logout
from rest_framework import permissions, status, views
from rest_framework.response import Response
from .serializers import UserSerializer
# from .models import Credentials
from django.http import  JsonResponse , HttpResponse
from django.shortcuts import render ,redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


class SignUpView(views.APIView):
    def post(self, request):
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['Confirm password']
        if User.objects.filter(username=username).exists():
            messages.success(request, 'username already exist')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.success(request, 'email already exist')
            return redirect('signup')
        if password != confirm_password:
            messages.success(request, 'password not matched')
            return redirect('signup')
        else:
            serializer = UserSerializer(data={'email':email,'username':username , 'password' :password})
           
            if serializer.is_valid():
                serializer.save()
                return redirect('signin')
            
    
    def get(self, request):
        return render(request, 'signup.html')

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
           
            # return render(request, 'index.html')
            # return redirect('/home')
            return redirect('index')
        else:
            messages.success(request, 'Invalid username or password.')
            return redirect('signin')
    else:
        return render(request, 'login.html')

@csrf_exempt
def logout_view(request):
    logout(request)
    return  redirect('index')
