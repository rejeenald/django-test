from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.sample.urls"))             # UI Kits Html files
]
