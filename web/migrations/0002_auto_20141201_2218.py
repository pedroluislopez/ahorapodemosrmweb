# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='blog',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Blog', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidato',
            name='facebook',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Facebook', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidato',
            name='podemos',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Perfil de Podemos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidato',
            name='twitter',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Twitter', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidato',
            name='youtube',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Youtube', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidato',
            name='descripcion_corta',
            field=models.CharField(max_length=100, verbose_name=b'Descripci\xc3\xb3n corta'),
            preserve_default=True,
        ),
    ]
