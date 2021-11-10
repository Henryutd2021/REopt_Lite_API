# Generated by Django 3.1.12 on 2021-11-10 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0135_remove_sitemodel_include_outage_emissions_in_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_cost_CO2',
            new_name='lifecycle_emissions_cost_CO2',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_cost_CO2_bau',
            new_name='lifecycle_emissions_cost_CO2_bau',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_cost_Health',
            new_name='lifecycle_emissions_cost_Health',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_cost_Health_bau',
            new_name='lifecycle_emissions_cost_Health_bau',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_lb_CO2',
            new_name='lifecycle_emissions_lb_CO2',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_lb_CO2_bau',
            new_name='lifecycle_emissions_lb_CO2_bau',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_lb_NOx',
            new_name='lifecycle_emissions_lb_NOx',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_lb_NOx_bau',
            new_name='lifecycle_emissions_lb_NOx_bau',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_lb_PM25',
            new_name='lifecycle_emissions_lb_PM25',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_lb_PM25_bau',
            new_name='lifecycle_emissions_lb_PM25_bau',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_lb_SO2',
            new_name='lifecycle_emissions_lb_SO2',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='lifetime_emissions_lb_SO2_bau',
            new_name='lifecycle_emissions_lb_SO2_bau',
        ),
        migrations.RenameField(
            model_name='sitemodel',
            old_name='preprocessed_lifetime_emissions_bau_lb_CO2',
            new_name='preprocessed_lifecycle_emissions_bau_lb_CO2',
        ),
    ]
