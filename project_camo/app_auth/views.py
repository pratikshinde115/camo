from django.contrib.auth import authenticate, login
from rest_framework import permissions, status, views
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Credentials
from django.http import  JsonResponse

class SignUpView(views.APIView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if Credentials.objects.filter(username=username).exists():
            return JsonResponse({'error': 'username already exist'}, status=400)
        if Credentials.objects.filter(email=email).exists():
            return JsonResponse({'error': 'email already exist'}, status=400)
        else:
            serializer = UserSerializer(data={'email':email,'username':username , 'password' :password})
            if serializer.is_valid():
                serializer.save()
    
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(views.APIView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = Credentials.objects.filter(username = username).first()

        if user is None:
             return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(password):
             return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message': 'You are now logged in.'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
