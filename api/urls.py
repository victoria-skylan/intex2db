from django.conf.urls import url, include
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api import views

urlpatterns = [
    path('campaigns/', views.CampaignList.as_view()),
    path('campaigns/<int:pk>/', views.CampaignDetail.as_view()),
    path('user/', views.CreateUser.as_view()),
]