# Generated by Django 5.0.7 on 2024-08-12 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_rename_image_testimonial_backgroundimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencyservice',
            name='background_image',
            field=models.ImageField(default='emergency_bg/default.png', upload_to='emergency_bg'),
        ),
    ]
