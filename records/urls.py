from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from records.views import RecordViewset
from django.conf import settings
from django.conf.urls.static import static

records_router = routers.DefaultRouter()
records_router.register('records',RecordViewset)
 
urlpatterns = [
    path('',include(records_router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
