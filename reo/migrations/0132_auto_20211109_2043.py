# Generated by Django 3.1.12 on 2021-11-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0131_auto_20211108_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemodel',
            name='annual_elec_kwh_for_testing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='annual_elec_kwh_for_testing_bau',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
