# Generated by Django 5.0.7 on 2024-08-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_equipment_service_equipments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.AddField(
            model_name='service',
            name='conclusion',
            field=models.TextField(default='hello'),
        ),
        migrations.AddField(
            model_name='service',
            name='introduction',
            field=models.TextField(default='Hello'),
        ),
    ]
