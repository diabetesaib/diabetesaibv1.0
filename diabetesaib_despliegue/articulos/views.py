#Este archivo se utiliza como referente para los demás

#Sde importa la librería render y las definiciones de los modelos
from django.shortcuts import render
from articulos.models import articulospost, categoriaarticulos

#Definimos las variables que se deberán concatenar en la url.py
def diabetesprofesional(request):
    #Seleccionamos todos los objetos (10 primeros) del modelo creado
    posts = articulospost.objects.all()[:10]
    posts1 = categoriaarticulos.objects.all()
    #Enviamos la información al template diabetesprofesiones.html y un diccionario para el html
    return render(request, "diabetesprofesiones.html", {'articulosposts':posts, 'p': posts1})

#definimos codigo_id que será el dato de la base de datos (que añade a la varibale del model: _id
#este dato se parará a la url <> que hayamos definido
def diabetesprofesionalextensa(request, codigo_id):
    #Debemos utilizar get para obtener el objeto que es único a esa especificación
    c= articulospost.objects.get(codigo=codigo_id)
    posts1 = categoriaarticulos.objects.all()
    posts2 = articulospost.objects.all()[:3]
    return render(request, 'diabetesprofesionalextensa.html', {'articulosposts': c, 'p': posts1, 'p1':posts2})

def categoriasdearticulos(request,categories_id):
    #filter permite filtrar, ideal para buscadores o agrupaciones en categorías
    posts = articulospost.objects.filter(categories=categories_id)[:10]
    posts1 = categoriaarticulos.objects.all()
    return render(request, "diabetesprofesionalescategorias.html", {'articulosposts':posts, 'p': posts1})