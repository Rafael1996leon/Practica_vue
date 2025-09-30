# crud_app/urls.py
from django.urls import path
from . import views # <-- ¡Esta línea es crucial!

urlpatterns = [
    path('', views.persona_list, name='persona_list'),
    path('nuevo/', views.persona_form, name='persona_create'),
    path('editar/<int:id>/', views.persona_form, name='persona_update'),
    path('eliminar/<int:id>/', views.persona_delete, name='persona_delete'),
]