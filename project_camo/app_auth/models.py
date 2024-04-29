from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Credentials(AbstractBaseUser):
    email = models.EmailField(default = "email",max_length=254, null=False)
    username = models.CharField(default = "username" , max_length=50 , null=False)
    password = models.CharField(default = "password",max_length=100,null = False)
    USERNAME_FIELD  = 'username'