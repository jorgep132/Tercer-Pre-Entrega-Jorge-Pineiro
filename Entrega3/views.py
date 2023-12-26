from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from Entrega3.models import Curso
from Entrega3.forms import (
        CursoFormulario,
        EstudiantesFormulario,
        EntregaFormulario,
        
            
)

# def buscar(request):
#     if request.GET["camada"]:
        
#         camada = request.GET['camada']
#         cursos = Curso.objects.filter(camada__icontains=camada)
        
#         return render(request, 'index.html', {'cursos':cursos, 'camada':camada})
#     else :
#         respuesta = 'No enviaste datos'
#         return render(request, 'index.html', {'respuesta':respuesta})

def buscar(request):
    camada = request.GET.get("camada")
    if camada is not None and camada !='':
        cursos = Curso.objects.filter(camada=camada)
        return render(request, 'index.html', {'cursos': cursos, 'camada': camada})
    else:
        respuesta = 'No enviaste datos válidos'
        return render(request, 'index.html', {'respuesta': respuesta})

def index(request):
    return render(request, 'index.html')


def formulario_curso (request):
    if request.method == 'POST':
        curso_form = CursoFormulario(request.POST)
        
        if curso_form.is_valid():
            nombre_curso = curso_form.cleaned_data['nombre_curso']
            camada = curso_form.cleaned_data['camada']
            curso_form.save()
            messages.success(request, f'El curso {nombre_curso} -- {camada} fue agregado exitosamente.')
            return redirect('index')
        
    else:
        curso_form = CursoFormulario()
        
    return render(request, 'cursos.html', {'curso_form':curso_form})


def vista_estudiantes(request):
    formulario_estudiantes = EstudiantesFormulario()
    
    if request.method == 'POST':
        formulario_estudiantes = EstudiantesFormulario(request.POST)
        
        if formulario_estudiantes.is_valid():
            nombre_estudiante = formulario_estudiantes.cleaned_data['nombre_estudiante']
            apellido_estudiante = formulario_estudiantes.cleaned_data['apellido_estudiante']
            formulario_estudiantes.save()
            messages.success(request, f'El estudiante {nombre_estudiante} {apellido_estudiante} fue registrado exitosamente.')
            return redirect('index')
        
    else:
        formulario_estudiantes = EstudiantesFormulario()
        
    return render(request, 'estudiantes.html', {'formulario_estudiantes': formulario_estudiantes})


def vista_entrega(request):
    formulario_entrega = EntregaFormulario()
    
    if request.method == 'POST':
        formulario_entrega = EntregaFormulario(request.POST)
        
        if formulario_entrega.is_valid():
            formulario_entrega.save()
            messages.success(request, f'La entrega se realizó exitosamente.')
            return redirect('index')
        
    else:
        formulario_entrega = EntregaFormulario()
        
    return render(request, 'entregables.html', {'formulario_entrega': formulario_entrega})


