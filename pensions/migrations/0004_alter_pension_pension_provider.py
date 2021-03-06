# Generated by Django 3.2.9 on 2022-01-19 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pensions', '0003_alter_pension_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pension',
            name='pension_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='recorded_pensions', to='pensions.provider'),
        ),
    ]
