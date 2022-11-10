from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aadharfront/', views.aadharfront, name="aadhar-front"),
    path('aadharback/', views.aadharback, name="aadhar-back"),
    path('pan', views.pan, name="pan"),
    path('bankstatement',views.bank, name="bank")
]