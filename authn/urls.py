
from django.urls import path

from . import views

app_name = 'authn'

urlpatterns = [

    path('signupuser/', views.signupuser, name='signupuser'),

    path('loginuser/', views.loginuser, name='loginuser'),
] 