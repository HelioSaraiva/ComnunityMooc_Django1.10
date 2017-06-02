# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 21:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de Usuário só pode conter letras, digitos ou osseguintes caracteres: @/./+/-/_', 'invalid')], verbose_name='Nome do Usuário'),
        ),
    ]
