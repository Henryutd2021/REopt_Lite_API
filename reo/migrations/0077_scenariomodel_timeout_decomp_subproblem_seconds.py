# Generated by Django 2.2.13 on 2020-09-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0076_auto_20200916_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenariomodel',
            name='timeout_decomp_subproblem_seconds',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
