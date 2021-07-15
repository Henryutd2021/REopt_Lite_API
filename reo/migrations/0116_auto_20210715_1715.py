# Generated by Django 3.1.12 on 2021-07-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0115_scenariomodel_include_climate_in_objective'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemodel',
            name='lifetime_emissions_cost_CO2_bau',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='lifetime_emissions_lb_CO2_bau',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
