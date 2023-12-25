from django import forms
from Entrega3.models import Curso

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'nombre_curso',
            'camada'
        ]