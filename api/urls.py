from django.contrib import admin
from django.urls import path,include
from freeContent.views import Register,Login
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register(r'register',Register,basename='user')

urlpatterns = [
    path('',include(routers.urls)),
    path('login/',Login.as_view())
]
