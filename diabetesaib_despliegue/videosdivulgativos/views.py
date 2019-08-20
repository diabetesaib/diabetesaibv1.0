from django.shortcuts import render
from videosdivulgativos.models import videosdivulgativospost, videosdivulgativoscategorias

def videosdivulgativos(request):
    posts = videosdivulgativospost.objects.all()[:10]
    posts1 = videosdivulgativoscategorias.objects.all()
    return render(request, 'videosdivulgativos.html', {'videos':posts, 'p':posts1})

def videosdivulgativoscategoriasvista(request,categories_id):
    posts = videosdivulgativospost.objects.filter(categories=categories_id)

    posts1 = videosdivulgativoscategorias.objects.all()

    return render(request, "videosdivulgativoscategorias.html", {'videos':posts, 'p': posts1})