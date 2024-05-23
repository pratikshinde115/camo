
from django.urls import path , include
from . import views 

from django.urls import path
from .views import SignUpView, SignInView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('reset_password/', include('django.contrib.auth.urls')),
]
