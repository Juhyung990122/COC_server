from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('coc-admin/', admin.site.urls),
    path('', include('users.urls')),
    path('',include('books.urls')),
    path('',include('records.urls'))
]
