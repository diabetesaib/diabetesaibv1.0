from django.contrib import admin

from reflexiones.models import reflexionespost, reflexionescategorias

class reflexionescategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class reflexionespostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(reflexionescategorias,reflexionescategoriasAdmin)
admin.site.register(reflexionespost, reflexionespostAdmin)