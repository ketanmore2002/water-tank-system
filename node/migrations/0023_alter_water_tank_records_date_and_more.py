# Generated by Django 4.1.5 on 2023-08-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0022_water_tank_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water_tank_records',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='water_tank_records',
            name='run_time_today',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='water_tank_records',
            name='stop_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='water_tank_records',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='water_tank_records_temp',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='water_tank_records_temp',
            name='run_time_today',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='water_tank_records_temp',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
