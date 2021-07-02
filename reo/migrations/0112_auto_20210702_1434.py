# Generated by Django 3.1.12 on 2021-07-02 14:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0111_auto_20210524_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadprofileboilerfuelmodel',
            name='addressable_load_fraction',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='loadprofileboilerfuelmodel',
            name='dhw_fraction_of_addressable_load',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, null=True, size=None),
        ),
        migrations.AddField(
            model_name='loadprofileboilerfuelmodel',
            name='space_heating_fraction_of_addressable_load',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, null=True, size=None),
        ),
    ]
