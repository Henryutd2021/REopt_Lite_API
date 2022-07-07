# Generated by Django 4.0.4 on 2022-07-07 21:02

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_electricstorageoutputs_initial_capital_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electrictariffinputs',
            name='coincident_peak_load_active_timesteps',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_chp_standby_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_coincident_peak_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_coincident_peak_cost_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_demand_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_demand_cost_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_energy_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_energy_cost_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_export_benefit',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_export_benefit_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_fixed_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_fixed_cost_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_min_charge_adder',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='lifecycle_min_charge_adder_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_bill',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_bill_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_chp_standby_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_coincident_peak_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_coincident_peak_cost_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_demand_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_demand_cost_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_energy_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_energy_cost_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_export_benefit',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_export_benefit_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_fixed_cost',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_fixed_cost_bau',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_min_charge_adder',
        ),
        migrations.RemoveField(
            model_name='electrictariffoutputs',
            name='year_one_min_charge_adder_bau',
        ),
        migrations.RemoveField(
            model_name='financialoutputs',
            name='lifecycle_capital_costs_plus_om',
        ),
        migrations.RemoveField(
            model_name='financialoutputs',
            name='lifecycle_om_costs_bau',
        ),
        migrations.RemoveField(
            model_name='generatoroutputs',
            name='fuel_used_gal',
        ),
        migrations.RemoveField(
            model_name='generatoroutputs',
            name='lifecycle_fixed_om_cost',
        ),
        migrations.RemoveField(
            model_name='generatoroutputs',
            name='lifecycle_fuel_cost',
        ),
        migrations.RemoveField(
            model_name='generatoroutputs',
            name='lifecycle_variable_om_cost',
        ),
        migrations.RemoveField(
            model_name='generatoroutputs',
            name='year_one_fixed_om_cost',
        ),
        migrations.RemoveField(
            model_name='generatoroutputs',
            name='year_one_fuel_cost',
        ),
        migrations.RemoveField(
            model_name='generatoroutputs',
            name='year_one_variable_om_cost',
        ),
        migrations.RemoveField(
            model_name='pvoutputs',
            name='lifecycle_om_cost',
        ),
        migrations.RemoveField(
            model_name='windoutputs',
            name='lifecycle_om_cost',
        ),
        migrations.RemoveField(
            model_name='windoutputs',
            name='year_one_om_cost',
        ),
        migrations.AddField(
            model_name='electricloadinputs',
            name='min_load_met_annual_pct',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='electricloadinputs',
            name='operating_reserve_required_pct',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='electricloadoutputs',
            name='offgrid_annual_oper_res_provided_series_kwh',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, help_text='Total operating reserves provided on an annual basis, for off-grid scenarios only', size=None),
        ),
        migrations.AddField(
            model_name='electricloadoutputs',
            name='offgrid_annual_oper_res_required_series_kwh',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, help_text='Total operating reserves required on an annual basis, for off-grid scenarios only', size=None),
        ),
        migrations.AddField(
            model_name='electricloadoutputs',
            name='offgrid_load_met_pct',
            field=models.FloatField(blank=True, help_text='Percentage of total electric load met on an annual basis, for off-grid scenarios only', null=True),
        ),
        migrations.AddField(
            model_name='electricloadoutputs',
            name='offgrid_load_met_series_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, help_text='Percentage of total electric load met on an annual basis, for off-grid scenarios only', size=None),
        ),
        migrations.AddField(
            model_name='electrictariffinputs',
            name='coincident_peak_load_active_time_steps',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), blank=True, default=list, size=None, validators=[django.core.validators.MinValueValidator(1)]), blank=True, default=list, help_text='The optional coincident_peak_load_charge_per_kw will apply to the max grid-purchased power during these time steps. Note time steps are indexed to a base of 1 not 0.', size=None),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_chp_standby_cost_after_tax',
            field=models.FloatField(blank=True, help_text='Optimal life cycle standby charge cost incurred by CHP, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_coincident_peak_cost_after_tax',
            field=models.FloatField(blank=True, help_text='Optimal total coincident peak charges over the analysis period, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_coincident_peak_cost_after_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual life cycle coincident peak charges, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_demand_cost_after_tax',
            field=models.FloatField(blank=True, help_text='Optimal life cycle utility demand cost, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_demand_cost_after_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual life cycle lifecycle utility demand cost, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_energy_cost_after_tax',
            field=models.FloatField(blank=True, help_text='Optimal life cycle utility energy cost, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_energy_cost_after_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual life cycle utility energy cost, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_export_benefit_after_tax',
            field=models.FloatField(blank=True, help_text='Optimal life cycle value of exported energy, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_export_benefit_after_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual life cycle value of exported energy, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_fixed_cost_after_tax',
            field=models.FloatField(blank=True, help_text='Optimal life cycle utility fixed cost, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_fixed_cost_after_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual life cycle utility fixed cost, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_min_charge_adder_after_tax',
            field=models.FloatField(blank=True, help_text='Optimal life cycle utility minimum charge adder, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='lifecycle_min_charge_adder_after_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual life cycle utility minimum charge adder, after-tax', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_bill_before_tax',
            field=models.FloatField(blank=True, help_text='Optimal year one utility bill', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_bill_before_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual year one utility bill', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_chp_standby_cost_before_tax',
            field=models.FloatField(blank=True, help_text='Optimal year one standby charge cost incurred by CHP', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_coincident_peak_cost_before_tax',
            field=models.FloatField(blank=True, help_text='Optimal year one coincident peak charges', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_coincident_peak_cost_before_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual year one coincident peak charges', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_demand_cost_before_tax',
            field=models.FloatField(blank=True, help_text='Optimal year one utility demand cost', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_demand_cost_before_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual year one utility demand cost', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_energy_cost_before_tax',
            field=models.FloatField(blank=True, help_text='Optimal year one utility energy cost', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_energy_cost_before_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual year one utility energy cost', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_export_benefit_before_tax',
            field=models.FloatField(blank=True, help_text='Optimal year one value of exported energy', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_export_benefit_before_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual year one value of exported energy', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_fixed_cost_before_tax',
            field=models.FloatField(blank=True, help_text='Optimal year one utility fixed cost', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_fixed_cost_before_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual year one utility fixed cost', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_min_charge_adder_before_tax',
            field=models.FloatField(blank=True, help_text='Optimal year one utility minimum charge adder', null=True),
        ),
        migrations.AddField(
            model_name='electrictariffoutputs',
            name='year_one_min_charge_adder_before_tax_bau',
            field=models.FloatField(blank=True, help_text='Business as usual year one utility minimum charge adder', null=True),
        ),
        migrations.AddField(
            model_name='financialinputs',
            name='offgrid_other_annual_costs',
            field=models.FloatField(blank=True, default=0.0, help_text='Only applicable when off_grid_flag is true. Considered tax deductible for owner. Costs are per year.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000.0)]),
        ),
        migrations.AddField(
            model_name='financialinputs',
            name='offgrid_other_capital_costs',
            field=models.FloatField(blank=True, default=0.0, help_text='Only applicable when off_grid_flag is true, applies a straight-line depreciation to this capex cost, reducing taxable income.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000.0)]),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_MG_upgrade_and_fuel_cost',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this is the cost to upgrade generation and storage technologies to be included in microgridplus present value of microgrid fuel costs.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_capital_costs_plus_om_after_tax',
            field=models.FloatField(blank=True, help_text='Capital cost for all technologies plus present value of operations and maintenance over anlaysis period', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_chp_standby_cost_after_tax',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this value is the present value of all CHP standby charges, after tax.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_elecbill_after_tax',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this value is the present value of all electric utility charges, after tax.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_fuel_costs_after_tax',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this value is the present value of all fuel costs over the analysis period, after tax.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_generation_tech_capital_costs',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this value is the net capital costs for all generation technologiesCosts are given in present value, including replacement costs and incentives.This value does not include offgrid_other_capital_costs.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_offgrid_other_annual_costs_after_tax',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this value is the present value of offgrid_other_annual_costs over the analysis period, after tax.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_offgrid_other_capital_costs',
            field=models.FloatField(blank=True, help_text="Component of lifecycle costs, this value is equal to offgrid_other_capital_costs with straight line depreciation applied over analysis period. The depreciation expense is assumed to reduce the owner's taxable income.", null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_om_costs_before_tax_bau',
            field=models.FloatField(blank=True, help_text='Business-as-usual present value of operations and maintenance over analysis period', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_outage_cost',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, expected outage cost.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_production_incentive_after_tax',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this value is the present value of all production-based incentives, after tax.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='lifecycle_storage_capital_costs',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this value is the Net capital costs for all storage technologiesValue is in present value, including replacement costs and incentives.This value does not include offgrid_other_capital_costs.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='offgrid_microgrid_lcoe_dollars_per_kwh',
            field=models.FloatField(blank=True, help_text='Levelized cost of electricity for modeled off-grid system.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='replacements_future_cost_after_tax',
            field=models.FloatField(blank=True, help_text='Future cost of replacing storage and/or generator systems, after tax.', null=True),
        ),
        migrations.AddField(
            model_name='financialoutputs',
            name='replacements_present_cost_after_tax',
            field=models.FloatField(blank=True, help_text='Present value cost of replacing storage and/or generator systems, after tax.', null=True),
        ),
        migrations.AddField(
            model_name='generatorinputs',
            name='replace_cost_per_kw',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000.0)]),
        ),
        migrations.AddField(
            model_name='generatorinputs',
            name='replacement_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='generatoroutputs',
            name='average_annual_fuel_used_gal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatoroutputs',
            name='lifecycle_fixed_om_cost_after_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatoroutputs',
            name='lifecycle_fuel_cost_after_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatoroutputs',
            name='lifecycle_variable_om_cost_after_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatoroutputs',
            name='year_one_fixed_om_cost_before_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatoroutputs',
            name='year_one_fuel_cost_before_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatoroutputs',
            name='year_one_variable_om_cost_before_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvinputs',
            name='operating_reserve_required_pct',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AddField(
            model_name='pvoutputs',
            name='lifecycle_om_cost_after_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='off_grid_flag',
            field=models.BooleanField(blank=True, default=False, help_text='Set to true to enable off-grid analyses'),
        ),
        migrations.AddField(
            model_name='windoutputs',
            name='lifecycle_om_cost_after_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='windoutputs',
            name='year_one_om_cost_before_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='electricloadinputs',
            name='critical_load_pct',
            field=models.FloatField(blank=True, help_text='Critical load factor is multiplied by the typical load to determine the critical load that must be met during an outage. Value must be between zero and one, inclusive.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='electricstorageinputs',
            name='can_grid_charge',
            field=models.BooleanField(blank=True, help_text='Flag to set whether the battery can be charged from the grid, or just onsite generation.'),
        ),
        migrations.AlterField(
            model_name='electricstorageinputs',
            name='soc_init_pct',
            field=models.FloatField(blank=True, help_text='Battery state of charge at first hour of optimization as fraction of energy capacity.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='electrictariffinputs',
            name='coincident_peak_load_charge_per_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000.0)]), blank=True, default=list, help_text='Optional coincident peak demand charge that is applied to the max load during the time_steps specified in coincident_peak_load_active_time_steps', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='financialinputs',
            name='microgrid_upgrade_cost_pct',
            field=models.FloatField(blank=True, help_text='Additional cost, in percent of non-islandable capital costs, to make a distributed energy system islandable from the grid and able to serve critical loads. Includes all upgrade costs such as additional laber and critical load panels.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='financialoutputs',
            name='lifecycle_om_costs_after_tax',
            field=models.FloatField(blank=True, help_text='Component of lifecycle costs, this value is the present value of all O&M costs, after tax.', null=True),
        ),
        migrations.AlterField(
            model_name='generatorinputs',
            name='fuel_avail_gal',
            field=models.FloatField(blank=True, help_text='On-site generator fuel available in gallons.', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000000.0)]),
        ),
        migrations.AlterField(
            model_name='generatorinputs',
            name='min_turn_down_pct',
            field=models.FloatField(blank=True, help_text='Minimum generator loading in percent of capacity (size_kw).', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='pvinputs',
            name='can_export_beyond_nem_limit',
            field=models.BooleanField(blank=True, help_text='True/False for if technology can export energy beyond the annual site load (and be compensated for that energy at the export_rate_beyond_net_metering_limit).'),
        ),
        migrations.AlterField(
            model_name='pvinputs',
            name='can_net_meter',
            field=models.BooleanField(blank=True, help_text='True/False for if technology has option to participate in net metering agreement with utility. Note that a technology can only participate in either net metering or wholesale rates (not both).'),
        ),
        migrations.AlterField(
            model_name='pvinputs',
            name='can_wholesale',
            field=models.BooleanField(blank=True, help_text='True/False for if technology has option to export energy that is compensated at the wholesale_rate. Note that a technology can only participate in either net metering or wholesale rates (not both).'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='run_bau',
            field=models.BooleanField(blank=True, default=True, help_text='If True then the Business-As-Usual scenario is also solved to provide additional outputs such as the LCC and BAU costs.', null=True),
        ),
    ]
