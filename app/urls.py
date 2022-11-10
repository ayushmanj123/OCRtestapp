from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aadharfront/', views.aadharfront, name="aadhar-front")
]