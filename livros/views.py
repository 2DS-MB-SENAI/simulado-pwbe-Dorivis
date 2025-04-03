# livros/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Livro
from .serializers import LivroSerializer

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})


@api_view(['GET', 'POST'])
def livros_api(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)