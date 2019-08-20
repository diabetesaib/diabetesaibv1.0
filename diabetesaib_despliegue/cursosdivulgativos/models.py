from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class cursosdivulgativospost(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    title = models.CharField(max_length=65, verbose_name="Cabecera")
    metacontent = models.CharField(max_length=150, verbose_name="Descripción en google")
    descripcion = RichTextField(max_length=1000, verbose_name="Descripción ligera")
    imagen = models.ImageField(verbose_name="Miniatura", blank=True, null=True, upload_to="cursosprofesionales")
    precio = models.CharField(max_length=60, verbose_name="Precio sin rebajar")
    descuento = models.CharField(max_length=60, verbose_name="Porcentaje descontado", null=True, blank=True)
    duracion = models.CharField(max_length=30, verbose_name="Duración del curso")
    contenido= models.CharField(max_length=100, verbose_name="Contenido del curso")
    explicacion = RichTextField(max_length=10000, verbose_name="Explicación del curso")
    requisitos= RichTextField(max_length=100, verbose_name="Requisitos del curso")
    titulovideo= models.CharField(max_length=100, verbose_name="Título del vídeo promocional")
    videoprincipal= models.CharField(max_length=1000,verbose_name="url del vídeo promocional")
    author= models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    codigo = models.CharField(max_length=300, verbose_name="codigo")
    adquisicion= models.CharField(max_length=1000, verbose_name="link para comprar curso", null=True, blank=True)
    masinformacion= RichTextField(max_length=1500, verbose_name="Información extra del curso", null=True, blank=True)

    class Meta:

        verbose_name = "Curso divulgativo"

        verbose_name_plural = "Cursos divulgativos"

        ordering = ['-created']

    def __str__(self):
        return self.titulo
