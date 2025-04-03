from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15)
    def __str__(self):
        return self.username