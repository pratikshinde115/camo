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


class SignUpView(views.APIView):
    def post(self, request):
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['Confirm password']
        print(email)
        if User.objects.filter(username=username).exists():
            return HttpResponse('username already exist', status=400)
        if User.objects.filter(email=email).exists():
            return HttpResponse('email already exist', status=400)
        if password != confirm_password:
            return HttpResponse('password not matched', status=400)
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
            print(request.user.is_authenticated)
            # return render(request, 'index.html')
            # return redirect('/home')
            return redirect('index')
        else:
            return HttpResponse('Invalid username or password.', status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request, 'login.html')

@csrf_exempt
def logout_view(request):
    logout(request)
    return  redirect('index')
