# Generated by Django 2.2.13 on 2021-03-01 18:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0101_auto_20210127_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatormodel',
            name='sr_provided_series_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='loadprofilemodel',
            name='min_load_met_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loadprofilemodel',
            name='sr_required_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loadprofilemodel',
            name='sr_required_series_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='sr_required_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='sr_required_series_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='offgrid_flag',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='storagemodel',
            name='sr_provided_series_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='sr_required_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='sr_required_series_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), default=list, null=True, size=None),
        ),
    ]
