from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15)
    
    # Campos adicionais para facilitar a autenticação
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['telefone']

    def __str__(self):
        return self.username