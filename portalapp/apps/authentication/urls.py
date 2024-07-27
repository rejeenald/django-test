# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from apps.authentication import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),


    #Tenant, Team, and User
    path('myteam/BJL192PPTTO92PP123PP/', views.myteam, name='myteam'),
    path('userprofile/BJL192PPTTO92PP123PP/', views.userprofile, name='userprofile'),

]
