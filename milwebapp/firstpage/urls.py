from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path("predictMPG",views.predictMPG,name="predictMPG")
]