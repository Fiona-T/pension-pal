# Generated by Django 3.2.9 on 2021-12-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employer_name',
            field=models.CharField(max_length=40),
        ),
    ]
