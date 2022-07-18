# Generated by Django 4.0.6 on 2022-07-15 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_pvoutputs_lifecycle_om_cost_after_tax_bau'),
    ]

    operations = [
        migrations.AddField(
            model_name='existingboilerinputs',
            name='emissions_factor_lb_CO2_per_mmbtu',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000000.0)]),
        ),
        migrations.AddField(
            model_name='existingboilerinputs',
            name='emissions_factor_lb_NOx_per_mmbtu',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000000.0)]),
        ),
        migrations.AddField(
            model_name='existingboilerinputs',
            name='emissions_factor_lb_PM25_per_mmbtu',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000000.0)]),
        ),
        migrations.AddField(
            model_name='existingboilerinputs',
            name='emissions_factor_lb_SO2_per_mmbtu',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000000.0)]),
        ),
    ]
