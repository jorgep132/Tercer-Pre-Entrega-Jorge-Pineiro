from django.http import HttpResponse
from django.shortcuts import render
from Entrega3.forms import CursoFormulario

def index(request):
    return render(request, 'index.html')

# def vista_curso(request):
#     return render(request, 'cursos.html')

def formulario_curso (request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoFormulario()
    return render(request, 'cursos.html', {'form':form})