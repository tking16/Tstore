# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-02 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('stock', models.IntegerField(default=70)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
    ]