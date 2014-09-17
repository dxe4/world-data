# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('code_3', models.CharField(max_length=3)),
                ('code_2', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CountryInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indicator_code', models.CharField(max_length=50)),
                ('indicator_name', models.CharField(max_length=50)),
                ('indicator_id', models.IntegerField(max_length=2, db_index=True)),
                ('years', models.TextField()),
                ('values', models.TextField()),
                ('color_map_values', models.TextField()),
                ('country', models.ManyToManyField(to='spam.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
