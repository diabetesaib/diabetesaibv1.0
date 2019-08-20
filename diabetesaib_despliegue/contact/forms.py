#Importamos la librería de formularios de Django
from django import forms

#Definimos el formulario que hereda de forms.Form
class formulario_contacto(forms.Form):
    #Definimos el usuario como un charfield, que es obligatorio (requiered=True)
    # se añade un textinput y un ayudador como placeholder
    usuario=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'placeholder':'Escribe aquí su nombre'}
    ))
    email=forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'placeholder':'Escribe aquí su correo'}
    ))
    content=forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'rows': 8, 'placeholder':'Escribe aquí su duda o sugerencia'}
    ))
