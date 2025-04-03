# usuarios/urls.py
from django.urls import path
from . import views  # Alternativa segura para evitar import circular

urlpatterns = [
    path('registro/', views.RegistrarView.as_view(), name='registro'),
    path('login/', views.LoginView.as_view(), name='login'),
]