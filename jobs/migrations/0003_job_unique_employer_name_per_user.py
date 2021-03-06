# Generated by Django 3.2.9 on 2022-01-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_employer_name'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='job',
            constraint=models.UniqueConstraint(fields=('added_by', 'employer_name'), name='unique_employer_name_per_user'),
        ),
    ]
