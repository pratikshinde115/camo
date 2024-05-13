
from django.urls import path , include
from . import views 

from django.urls import path
from .views import SignUpView, signin ,logout_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/' ,logout_view ,name ='logout')

    # path('reset_password/', include('django.contrib.auth.urls')),
]
