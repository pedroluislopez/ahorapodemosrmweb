# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20141201_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titular', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('resumen', models.TextField(max_length=1000, verbose_name=b'Resumen')),
                ('enlace', models.CharField(max_length=255, verbose_name=b'Enlace')),
                ('diario', models.CharField(max_length=50, verbose_name=b'Diario')),
                ('fecha', models.DateField(verbose_name=b'Fecha')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
