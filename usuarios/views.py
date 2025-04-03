# Certifique-se que estas imports estão corretas
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

class RegistrarView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LoginView(TokenObtainPairView):
    pass