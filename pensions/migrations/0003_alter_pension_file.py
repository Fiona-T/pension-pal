# Generated by Django 3.2.9 on 2021-12-22 15:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pensions', '0002_pension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pension',
            name='file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
