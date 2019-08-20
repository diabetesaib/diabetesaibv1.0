from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class reflexionescategorias(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nombre")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")



    class Meta:

        verbose_name = "categoría de reflexión"

        verbose_name_plural = "categorías de reflexiones"

        ordering = ['-created']



    def __str__(self):

        return self.name


class reflexionespost(models.Model):

    title = models.CharField(max_length=200, verbose_name="Título")

    title1 = models.CharField(max_length=65, verbose_name="Cabecera de Google")

    metacontent = models.CharField(max_length=150, verbose_name="Metacontent")

    descripcionbreve = RichTextField(max_length=2000, verbose_name="Descripción breve")

    content = RichTextField(verbose_name="Contenido")

    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)

    image = models.ImageField(verbose_name="Miniatura", upload_to="noticias", null=True, blank=True)

    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    codigo = models.CharField(max_length=300, verbose_name="Código")

    categories = models.ManyToManyField(reflexionescategorias, verbose_name="Categoría de reflexión")



    class Meta:

        verbose_name = "Reflexión"

        verbose_name_plural = "Reflexiones"

        ordering = ['-created']



    def __str__(self):

        return self.title