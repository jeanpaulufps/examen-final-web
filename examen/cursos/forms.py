from django import forms

class MatricularEstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    email = forms.EmailField()
