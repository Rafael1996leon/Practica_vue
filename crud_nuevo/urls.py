# crud_nuevo/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # PASO 1: Redirigir la raíz (/) a la aplicación 'crud_app'
    path('', include('crud_app.urls')),
]