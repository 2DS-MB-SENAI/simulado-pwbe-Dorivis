from django.urls import path
from .views import listar_livros, livros_api  # Importe a view corretamente

urlpatterns = [
    path('livros/', listar_livros, name='listar_livros'),
    path('api/livros/', livros_api, name='livros-api'),
]