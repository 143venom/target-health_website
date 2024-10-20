# Generated by Django 5.0.7 on 2024-08-08 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_department_remove_appointment_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.department'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctorteam'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
