# Generated by Django 5.0.7 on 2024-08-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_sitecontent_company_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecontent',
            name='company_address',
            field=models.CharField(max_length=150),
        ),
    ]
