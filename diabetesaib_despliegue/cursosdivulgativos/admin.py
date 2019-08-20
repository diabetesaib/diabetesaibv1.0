from django.contrib import admin
from cursosdivulgativos.models import cursosdivulgativospost

class cursosdivulgativosAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

    list_display = ('titulo', 'author')

    ordering = ('author', 'titulo')

    search_fields = ('titulo','author__username')





admin.site.register(cursosdivulgativospost, cursosdivulgativosAdmin)
