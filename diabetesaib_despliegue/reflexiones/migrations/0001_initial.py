# Generated by Django 2.1.4 on 2019-08-06 14:20

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='reflexionescategorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'categoría de reflexión',
                'verbose_name_plural': 'categorías de reflexiones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='reflexionespost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('title1', models.CharField(max_length=65, verbose_name='Cabecera de Google')),
                ('metacontent', models.CharField(max_length=150, verbose_name='Metacontent')),
                ('descripcionbreve', ckeditor.fields.RichTextField(max_length=2000, verbose_name='Descripción breve')),
                ('content', ckeditor.fields.RichTextField(max_length=2000, verbose_name='Contenido')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('image', models.ImageField(blank=True, null=True, upload_to='noticias', verbose_name='Miniatura')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('codigo', models.CharField(max_length=300, verbose_name='Código')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categories', models.ManyToManyField(to='reflexiones.reflexionescategorias', verbose_name='Categoría de reflexión')),
            ],
            options={
                'verbose_name': 'Reflexión',
                'verbose_name_plural': 'Reflexiones',
                'ordering': ['-created'],
            },
        ),
    ]
