# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name=b'Apellidos')),
                ('imagen', models.ImageField(upload_to=b'profile_images', verbose_name=b'Imagen', blank=True)),
                ('secretario', models.BooleanField(default=False, verbose_name=b'Secretario General')),
                ('consejo', models.BooleanField(default=False, verbose_name=b'Consejo Ciudadano')),
                ('descripcion_corta', models.CharField(max_length=50, verbose_name=b'Descripci\xc3\xb3n corta')),
                ('motivacion', models.TextField(max_length=1000, verbose_name=b'Motivaci\xc3\xb3n', blank=True)),
                ('orden', models.IntegerField(verbose_name=b'Orden')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cita', models.TextField(max_length=500, verbose_name=b'Cita')),
                ('orden', models.IntegerField(verbose_name=b'Orden')),
                ('candidato', models.ForeignKey(to='web.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('categoria', models.CharField(max_length=2, verbose_name=b'Categor\xc3\xada', choices=[(b'd', b'Documento'), (b'o', b'Octavilla'), (b's', b'Sin categor\xc3\xada')])),
                ('imagen', models.ImageField(upload_to=b'document_images', verbose_name=b'Imagen')),
                ('documento', models.FileField(upload_to=b'document_documents', verbose_name=b'Documento', blank=True)),
                ('orden', models.IntegerField(verbose_name=b'Orden')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IdeaFuerza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50, verbose_name=b'T\xc3\xadtulo')),
                ('seccion', models.CharField(max_length=2, verbose_name=b'Secci\xc3\xb3n', choices=[(b'm', b'M\xc3\xa9todo'), (b'p', b'Podemos Murcia'), (b'a', b'Ayuntamiento')])),
                ('icono', models.CharField(max_length=20, verbose_name=b'Icono')),
                ('descripcion', models.TextField(max_length=500, verbose_name=b'Descripci\xc3\xb3n')),
                ('orden', models.IntegerField(verbose_name=b'Orden')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
