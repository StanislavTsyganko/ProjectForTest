# Generated by Django 5.2.4 on 2025-07-12 13:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citate', '0002_citata_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='citata',
            name='raiting',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='citata',
            name='weight',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
