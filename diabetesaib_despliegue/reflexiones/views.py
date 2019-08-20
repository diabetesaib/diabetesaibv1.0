from django.shortcuts import render
from reflexiones.models import reflexionespost, reflexionescategorias
# Create your views here.

def listareflexionesvista(request):
    posts = reflexionespost.objects.all
    posts1 = reflexionescategorias.objects.all()
    return render(request, 'reflexiones.html', {'posts':posts, 'p':posts1})

def detallereflexionesvista(request, codigo_id):
    c = reflexionespost.objects.get(codigo=codigo_id)
    posts1 = reflexionescategorias.objects.all()
    return render(request, 'reflexionesextensas.html', {'posts': c, 'p':posts1})

def reflexionescategoriasvista(request, categories_id):
    posts= reflexionespost.objects.filter(categories=categories_id)
    posts1= reflexionescategorias.objects.all()
    return render(request, 'reflexionescategoria.html', {'posts': posts, 'p':posts1})
