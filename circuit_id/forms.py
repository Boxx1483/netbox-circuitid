from django import forms
from .models import CircuitID, CableCircuitID
from dcim.models import Cable

class CircuitIDForm(forms.ModelForm):
    class Meta:
        model = CircuitID
        fields = ['name', 'description']

class CableCircuitIDForm(forms.ModelForm):
    class Meta:
        model = CableCircuitID
        fields = ['cable', 'circuit_id']
