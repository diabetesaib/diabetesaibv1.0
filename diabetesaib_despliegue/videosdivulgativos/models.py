from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class videosdivulgativoscategorias(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de categoría")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría vídeo divulgativo"
        verbose_name_plural = "categorías vídeos divulgativos"

    def __str__(self):
        return self.nombre

class videosdivulgativospost(models.Model):
    title = models.CharField(max_length=20000,verbose_name="Cabecera página web")
    metacontent= models.CharField(max_length=1500,verbose_name="Descripción página web")
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descripcion = RichTextField(verbose_name="Descripción")
    url = models.CharField(max_length=1000, verbose_name="URL")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    categories = models.ManyToManyField(videosdivulgativoscategorias, verbose_name="Categorías de vídeos divulgativos")

    class Meta:

        verbose_name = "Video divulgativo"

        verbose_name_plural = "Vídeos divulgativos"

        ordering = ['-created']

    def __str__(self):
        return self.titulo

