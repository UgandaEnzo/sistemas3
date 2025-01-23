# Generated by Django 4.0.1 on 2025-01-21 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('website', models.URLField(max_length=120)),
                ('comentario', models.TextField()),
                ('fecha_creacion', models.DateTimeField(default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('costo', models.FloatField()),
                ('descripcion_corta', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('fecha_creacion', models.DateField(default=datetime.date.today)),
                ('disponible', models.BooleanField(default=True)),
                ('cantidad', models.IntegerField(default=100)),
                ('enlace', models.URLField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products Dell',
            },
        ),
        migrations.CreateModel(
            name='Registro_becado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('genero', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=10)),
                ('f_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=150)),
                ('telefono1', models.CharField(max_length=12)),
                ('telefono2', models.CharField(blank=True, max_length=12)),
                ('ubicacion', models.CharField(max_length=100)),
                ('carrera', models.CharField(max_length=100)),
                ('cede', models.CharField(max_length=100)),
                ('cursando', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('t_beneficio', models.CharField(max_length=100)),
                ('estatus', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('comentario', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('costo', models.FloatField(default=0.0)),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services Dell',
            },
        ),
        migrations.CreateModel(
            name='solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=8, unique=True)),
                ('edad', models.IntegerField()),
                ('f_nacimiento', models.DateField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('genero', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=10)),
                ('residencia', models.CharField(max_length=100)),
                ('comentario', models.TextField(blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.date.today)),
                ('carrera', models.CharField(default='none', max_length=100)),
                ('reporte_de_notas', models.FileField(blank=True, null=True, upload_to='pdfs/')),
            ],
        ),
    ]