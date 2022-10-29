from cgitb import html
from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name= 'login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('welcome/', views.welcome, name='welcome'),
    path('sair/', views.sair, name="sair")   
]