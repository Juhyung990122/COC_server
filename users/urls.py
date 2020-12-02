from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from users.views import UserViewset
from django.conf import settings
from django.conf.urls.static import static

users_router = routers.DefaultRouter()
users_router.register('users',UserViewset)
 
urlpatterns = [
    path('',include(users_router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
