from django.contrib import admin
from django.urls import path
from contact.views import formulario




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', formulario, name="formulario"),
]