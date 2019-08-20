from django.shortcuts import render
from cursosdivulgativos.models import cursosdivulgativospost
# Create your views here.
def cursosdivulgativos(request):
    post = cursosdivulgativospost.objects.all()
    return render(request, 'cursos.html', {'cursos':post})

def cursosdivulgativosextensos(request, codigo_id):
    c= cursosdivulgativospost.objects.get(codigo=codigo_id)
    return render(request, 'cursosextensos.html', {'cursos': c})