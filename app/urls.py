from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aadhar',views.aadhar, name="aadhar"),
    path('pan', views.pan, name="pan"),
    path('bankstatement',views.bank, name="bank")
]