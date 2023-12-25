from django.db import models

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=20)
    camada = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre_curso} -- {self.camada}'