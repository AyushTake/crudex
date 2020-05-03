from django.urls import path 
from urs import views

urlpatterns =[
    path('register',views.register),
    path('',views.home),
    path('login',views.login),
] 

