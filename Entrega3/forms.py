from django import forms
from Entrega3.models import(
    Curso,
    Estudiante,
    Entrega,
    
)

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'nombre_curso',
            'camada'
        ]
class EstudiantesFormulario(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__' 
        
class EntregaFormulario(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = '__all__'
        widgets = {
            'entregado': forms.CheckboxInput(),
        }  



