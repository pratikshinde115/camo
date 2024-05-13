# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.hashers import check_password
# from .models import Credentials
# from django.contrib.auth.models import User

# class CredentialsBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user = Credentials.objects.filter(username=username).first()
#             if user is not None:
#                 if user and check_password(password, user.password):
#                     return user  # Authenticate regular users
#             else:
#                 print("User does not exist.")  # Print if user is None
#                 return None
#         except Exception as e:
#             # Handle other exceptions
#             print(f"An error occurred: {e}")
#             return None
