from django.urls import path
from Entrega3.views import( 
    index,
    formulario_curso,
    vista_estudiantes,
    vista_entrega,
    
)

urlpatterns = [
    path('', index, name='index'),
    path('cursos/', formulario_curso, name='cursos'),
    path('estudiantes/', vista_estudiantes, name='estudiantes'),
    path('entregables/', vista_entrega, name='entregables'),

    
]
