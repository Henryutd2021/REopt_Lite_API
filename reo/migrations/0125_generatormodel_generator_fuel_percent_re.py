# Generated by Django 3.1.12 on 2021-10-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0124_auto_20211021_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatormodel',
            name='generator_fuel_percent_RE',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
