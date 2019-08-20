#Se utiliza este modelo como modélico para los comentarios

#Importamos los models (por defecto), el tiempo para el created y un richtextfiel que ayudará a escribir código
#Html en el admin, además de importar la librería del usuario
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

#Definimos la clase de categoría y la de contenidos
class categoriaarticulos(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de categoría")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre


class articulospost(models.Model):

    #Definimos una variable que contendrá el título y aparecerá como un campo pequeño para escribir, se debe poner un max_length=
    title = models.CharField(max_length=2000, verbose_name="Título")

    cabecera = models.CharField(max_length=6500, verbose_name="cabecera de google")

    metacontenidos = models.CharField(max_length=3000, verbose_name="descripción de página")

    #Permite poner un campo donde escribir html en el admin, verbose_name se utiliza para orientar al administrador de qué campos e trata
    descripcion = RichTextField(verbose_name="Descripción ligera")

    content = RichTextField(verbose_name="Contenido")

    bibliografia = RichTextField(verbose_name="Bibliografía")

    #Permite seleccionar una fecha, por defecto está puesto en ahora
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)

    #Permite subir una página, hay que especificar en settigns donde guardarla. Null y blank significa que no son obligatorias
    image = models.ImageField(verbose_name="Miniatura", upload_to="articulos", null=True, blank=True)

    encabezado1 = models.CharField(max_length=2000, verbose_name="Encabezado1", null=True, blank=True)

    image1 = models.ImageField(verbose_name="Image1 para pósters de congresos", upload_to="articulos", null=True, blank=True)

    piedefigura1= models.CharField(max_length=10000, verbose_name="Pie de figura1", null=True, blank=True)

    encabezado2 = models.CharField(max_length=2000, verbose_name="Encabezado2", null=True, blank=True)

    image2 = models.ImageField(verbose_name="Image2", upload_to="articulos", null=True, blank=True)

    piedefigura2 = models.CharField(max_length=10000, verbose_name="Pie de figura2", null=True, blank=True)

    encabezado3 = models.CharField(max_length=2000, verbose_name="Encabezado3", null=True, blank=True)

    image3 = models.ImageField(verbose_name="Image3", upload_to="articulos", null=True, blank=True)

    piedefigura3 = models.CharField(max_length=10000, verbose_name="Pie de figura3", null=True, blank=True)

    encabezado4 = models.CharField(max_length=2000, verbose_name="Encabezado4", null=True, blank=True)

    image4 = models.ImageField(verbose_name="Image4", upload_to="articulos", null=True, blank=True)

    piedefigura4 = models.CharField(max_length=10000, verbose_name="Pie de figura4", null=True, blank=True)

    #Permite hacer una relación uno a uno, debe decirse a qué hace referencia(User) y obligatorio poner on_delete
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    codigo = models.CharField(max_length=3000, verbose_name="url")

    #Permite hacer relación muchos a muchos
    categories = models.ManyToManyField(categoriaarticulos, verbose_name="Categorías")

    encabezadovideo= models.CharField(max_length=1000, verbose_name="Encabezado del vídeo", null=True, blank=True)

    video = models.CharField(max_length=10000, verbose_name="url del vídeo", null=True, blank=True)

    descripcionvideo= RichTextField(verbose_name="Descripción del vídeo", null=True, blank=True)


    #Definimos con esta clase cómo se llamará nuestra sección dentro del admin
    class Meta:

        verbose_name = "Arículo"

        verbose_name_plural = "Artículos"

        ordering = ['-created']


    #Definimos cómo llamará Django a la clase, suele ser así:
    def __str__(self):

        return self.title
