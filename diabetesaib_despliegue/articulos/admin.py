# Se utilizará la app artículos como referente de comentarios para las demás aplicaciones que repitan contenido

#Importamos el admin(por defecto) y los modelos que queremos que salgan en el admin
from django.contrib import admin
from articulos.models import articulospost, categoriaarticulos

#Definimos dos clases, una para las clases y otra para el contenido
class categoriaarticulosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostarticulosAdmin(admin.ModelAdmin):

    #Esta casilla solo leerá las casillas de creado y subido del modelo
    readonly_fields = ('created', 'updated')

    #Aparecerá una lista en el admin con als casillas definidas en el model
    list_display = ('title', 'author', 'published')

    #Se ordenarán los registron en el admin siguiendo el orden descrito
    ordering = ('author', 'published')

    #El admin tendrá un buscador donde se podrá buscar por título, contenido y autor
    search_fields = ('title','content','author__username')

    date_hierarchy = 'published'

#Estos comandos permiten que se registre en el admin
admin.site.register(categoriaarticulos, categoriaarticulosAdmin)
admin.site.register(articulospost, PostarticulosAdmin)