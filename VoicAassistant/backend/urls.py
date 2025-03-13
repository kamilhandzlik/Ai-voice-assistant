from django.contrib import admin
from django.urls import path, include
from .views import ApiView

urlpatterns = [
    path("", ApiView.as_view(), name="api-home")
]