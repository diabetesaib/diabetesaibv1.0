from django.contrib import admin
from videosdivulgativos.models import videosdivulgativospost, videosdivulgativoscategorias

class videosdivulgativoscategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class videosdivulgativosAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

    list_display = ('titulo', 'author')

    ordering = ('author', 'titulo')

    search_fields = ('titulo','author__username')




admin.site.register(videosdivulgativoscategorias,videosdivulgativoscategoriasAdmin)
admin.site.register(videosdivulgativospost, videosdivulgativosAdmin)
