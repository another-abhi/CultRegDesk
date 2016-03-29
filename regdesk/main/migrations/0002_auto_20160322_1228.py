# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-22 06:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participation',
            name='registration',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='event',
        ),
        migrations.AddField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Event'),
        ),
        migrations.AddField(
            model_name='registration',
            name='participation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Participation'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='participent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Participent'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
