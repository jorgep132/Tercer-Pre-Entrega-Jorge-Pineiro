from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=20, blank=False)
    camada = models.IntegerField(
        unique=True,
        error_messages={
            'unique': 'El numero de camada que intenta registrar ya existe. \nPor favor, utiliza otro numero.'
        }
    )
    
    def __str__(self) -> str:
        return f'{self.nombre_curso} -- {self.camada}'
 
class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=20)
    apellido_estudiante = models.CharField(max_length=20)
    email_estudiante = models.EmailField(
            unique=True,
            error_messages={
                'unique': 'El correo electrónico que intenta ingresar ya se encuentra registrado.\nPor favor, utiliza otro.'
            }
    )
    def __str__(self) -> str:
        return f'Nombre del estudiante: {self.nombre_estudiante}{self.apellido_estudiante}. Email: {self.email_estudiante}'
    

class Entrega(models.Model):
    nombre_estudiante = models.CharField(max_length=20, blank=False)
    fecha_entrega = models.DateTimeField(blank=False)
    entregado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'Nombre del estudiante: {self.nombre_estudiante}. Fecha de entrega{self.fecha_entrega}. Entregado: {self.entregado}'