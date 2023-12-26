from django.http import HttpResponse
from django.shortcuts import render, redirect
from Entrega3.models import Curso
from Entrega3.forms import (
        CursoFormulario,
        EstudiantesFormulario,
        EntregaFormulario,
        
            
)

# Vista inicio
def index(request):
    return render(request, 'index.html')

# Vista para buscar curso por camada
def buscar(request):
    camada = request.GET.get("camada")
    if camada is not None and camada !='':
        cursos = Curso.objects.filter(camada=camada)
        return render(request, 'index.html', {'cursos': cursos, 'camada': camada})
    else:
        respuesta = 'No enviaste datos válidos'
        return render(request, 'index.html', {'respuesta': respuesta})

# Vista para cargar cursos con nombre y camada
def formulario_curso (request):
    if request.method == 'POST':
        curso_form = CursoFormulario(request.POST)
        
        if curso_form.is_valid():
            curso_form.save()
            return redirect('index')
        
    else:
        curso_form = CursoFormulario()
        
    return render(request, 'cursos.html', {'curso_form':curso_form})

# Vista para cargar estudiantes con nombre, apellido y email
def vista_estudiantes(request):
    formulario_estudiantes = EstudiantesFormulario()
    
    if request.method == 'POST':
        formulario_estudiantes = EstudiantesFormulario(request.POST)
        
        if formulario_estudiantes.is_valid():
            formulario_estudiantes.save()
            return redirect('index')
        
    else:
        formulario_estudiantes = EstudiantesFormulario()
        
    return render(request, 'estudiantes.html', {'formulario_estudiantes': formulario_estudiantes})

# Vista para cargar entregas, con nombre del estudiante, fecha de entrega y checkbox
def vista_entrega(request):
    formulario_entrega = EntregaFormulario()
    
    if request.method == 'POST':
        formulario_entrega = EntregaFormulario(request.POST)
        
        if formulario_entrega.is_valid():
            formulario_entrega.save()
            return redirect('index')
        
    else:
        formulario_entrega = EntregaFormulario()
        
    return render(request, 'entregables.html', {'formulario_entrega': formulario_entrega})


