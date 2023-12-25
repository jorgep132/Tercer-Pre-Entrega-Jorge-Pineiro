from django.urls import path
from Entrega3.views import( 
    index,
    formulario_curso,
)

urlpatterns = [
    path('', index, name='index'),
    path('cursos/', formulario_curso, name='cursos')
    
]
