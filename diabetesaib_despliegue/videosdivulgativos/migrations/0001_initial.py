# Generated by Django 2.1.4 on 2019-08-06 08:23

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='videosdivulgativoscategorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de categoría')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'categoría vídeo divulgativo',
                'verbose_name_plural': 'categorías vídeos divulgativos',
            },
        ),
        migrations.CreateModel(
            name='videosdivulgativospost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, verbose_name='Cabecera página web')),
                ('metacontent', models.CharField(max_length=150, verbose_name='Descripción página web')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descripcion', ckeditor.fields.RichTextField(max_length=1000, verbose_name='Descripción')),
                ('url', models.CharField(max_length=1000, verbose_name='URL')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categories', models.ManyToManyField(to='videosdivulgativos.videosdivulgativoscategorias', verbose_name='Categorías de vídeos divulgativos')),
            ],
            options={
                'verbose_name': 'Video divulgativo',
                'verbose_name_plural': 'Vídeos divulgativos',
                'ordering': ['-created'],
            },
        ),
    ]
