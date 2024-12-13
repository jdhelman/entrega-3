from django import forms
from .models import ObraSocial, PlanSalud, Afiliado

class ObraSocialForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = '__all__'


class PlanSaludForm(forms.ModelForm):
    class Meta:
        model = PlanSalud
        fields = '__all__'


class AfiliadoForm(forms.ModelForm):
    class Meta:
        model = Afiliado
        fields = '__all__'
