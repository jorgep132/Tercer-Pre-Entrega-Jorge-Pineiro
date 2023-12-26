from datetime import datetime
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
            'fecha_entrega': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),

        } 
    def clean(self):
        cleaned_data = super().clean()
        fecha_entrega = cleaned_data.get('fecha_entrega')
        año_actual = datetime.now().year

        if fecha_entrega and fecha_entrega.year != año_actual:
            self.add_error('fecha_entrega', 'La fecha de entrega no debe ser diferente al año actual.')

        return cleaned_data 



