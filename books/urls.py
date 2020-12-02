from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import BookViewset
from django.conf import settings
from django.conf.urls.static import static

book_router = routers.DefaultRouter()
book_router.register('books',BookViewset )

urlpatterns = [
    path('',include(book_router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
