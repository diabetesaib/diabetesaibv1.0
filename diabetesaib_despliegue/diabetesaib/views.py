
from django.shortcuts import render
from articulos.models import articulospost
#from blog.models import Post
from cursosdivulgativos.models import cursosdivulgativospost
#from cursosprofesionales.models import cursosprofesionalespost
from reflexiones.models import reflexionespost
#from videoscientificos.models import videoscientificospost
from videosdivulgativos.models import videosdivulgativospost



def inicio(request):
    post = articulospost.objects.all()[0]
    #post1 = Post.objects.all()[0]
    post2 = cursosdivulgativospost.objects.all()[0]
    #post3 = cursosprofesionalespost.objects.all()[0]
    post4 = reflexionespost.objects.all()[0]
    #post5 = videoscientificospost.objects.all()[0]
    post6 = videosdivulgativospost.objects.all()[0]
    return render(request, 'index.html', {'articulosposts': post,
                                                  #'noticias':post1,
                                                  'cursosdivulgativos':post2,
                                                  #'cursosprofesionales':post3,
                                                  'reflexiones':post4,
                                                  #'videoscientificos':post5,
                                                  'videosdivulgativos':post6})

def quienessomos(request):
    return render(request, 'quienesomos.html')

def politicadeprivacidad(request):
    return render(request, 'politicadeprivacidad.html')

def politicadecookies(request):
    return render(request, 'politicadecookies.html')

def diabetesprofesional (request):
    return render(request, 'diabetesprofesiones.html')

def videosdivulgativos (request):
    return render(request, 'videosdivulgativos.html')

def listareflexionesvista (request):
    return render (request, 'reflexiones.html')

def cursosdivulgativos (request):
    return render(request, 'cursos.html')

