"""diabetesaib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Importación de algunas librerias para las urls
from django.contrib import admin
from django.urls import path, include

#Importamos todas las clases y definiciones de las vistas, algunas se han dejado en comentarios por si se quiere ampliar en un futuro
from diabetesaib.views import inicio, quienessomos, politicadeprivacidad, politicadecookies
from articulos.views import diabetesprofesional, diabetesprofesionalextensa, categoriasdearticulos
from videosdivulgativos.views import videosdivulgativos, videosdivulgativoscategoriasvista
from cursosdivulgativos.views import cursosdivulgativos, cursosdivulgativosextensos
from reflexiones.views import listareflexionesvista, detallereflexionesvista, reflexionescategoriasvista
#from blog.views import diabetesdivulgativa, diabetesdivulgativaextensa, diabetesdivulgativacategoria
#from videoscientificos.views import videoscientificos, videoscientificoscategoriasvista
#from cursosprofesionales.views import cursosprofesionales, cursosprofesionalesextensos


#Para ver fotos en modo debug
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Aquí se encuentran las urls. La include tiene una carpeta views.py en su proyecto
# las que se encuentran en <> indica que en views.py la definición pasa un comando
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('que-es-diabetes-aib/', quienessomos, name="quienessomos"),
    path('formulario-de-contacto/', include('contact.urls')),
    path('politica-de-privacidad/', politicadeprivacidad, name="politicadeprivacidad"),
    path('politica-de-cookies/', politicadecookies, name="politicadecookies"),
    path('articulos/', diabetesprofesional, name="diabetesprofesional"),
    path('articulos/<codigo_id>/', diabetesprofesionalextensa, name="diabetesprofesionalextensa"),
    path('articulos/categorias/<categories_id>/', categoriasdearticulos, name="categoriaarticulos1"),
    path('cursos/', cursosdivulgativos, name="cursosdivulgativos"),
    path('cursos/<codigo_id>/', cursosdivulgativosextensos, name="cursosdivulgativosextensos"),
    path('videos/', videosdivulgativos, name="videosdivulgativos"),
    path('videos/categorias/<categories_id>/', videosdivulgativoscategoriasvista, name="videosdivulgativoscategorias"),
    path('reflexiones/', listareflexionesvista, name="listareflexiones"),
    path('reflexiones/<codigo_id>/', detallereflexionesvista, name="detallereflexiones"),
    path('reflexiones/categorias/<categories_id>/', reflexionescategoriasvista, name="reflexionescategoriasvista"),
    #Path de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),


    #Eliminadas de momento
    #path('conoce-la-diabetes/videos/', videoscientificos, name="videoscientificos"),
    #path('conoce-la-diabetes/videos/categorias/<categories_id>/', videoscientificoscategoriasvista,name="videoscientificoscategoriasvista"),
    #path('conoce-tu-diabetes/noticias/', diabetesdivulgativa, name="diabetesdivulgativa"),
    #path('conoce-tu-diabetes/noticias/<codigo_id>/', diabetesdivulgativaextensa, name="diabetesdivulgativaextensa"),
    #path('conoce-tu-diabetes/noticias/categorias/<categories_id>/', diabetesdivulgativacategoria, name="diabetesdivulgativacategoria"),
    #path('conoce-la-diabetes/cursos-para-profesionales/', cursosprofesionales, name="cursosprofesionales"),
    #path('conoce-la-diabetes/cursos-para-profesionales/<codigo_id>/', cursosprofesionalesextensos,name="cursosprofesionalesextensos"),
]

#Comandos necesarios para ver imágenes en modo debug true
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

