# Generated by Django 4.0.6 on 2022-09-19 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_rename_critical_load_pct_electricloadinputs_critical_load_fraction_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvinputs',
            old_name='prod_factor_series',
            new_name='production_factor_series',
        ),
        migrations.RenameField(
            model_name='windinputs',
            old_name='prod_factor_series',
            new_name='production_factor_series',
        ),
    ]
