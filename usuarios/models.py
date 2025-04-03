from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15)
    
    # Adicione related_name personalizados
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuarios_groups',  # Nome único
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuarios_permissions',  # Nome único
        related_query_name='usuario',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['telefone']

    def __str__(self):
        return self.username