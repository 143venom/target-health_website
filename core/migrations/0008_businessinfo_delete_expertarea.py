# Generated by Django 5.0.7 on 2024-08-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_expertarea_buttontext'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab', models.CharField(choices=[('Excellent Services', 'Excellent Services'), ('Qualified Doctors', 'Qualified Doctors'), ('Emergency Departments', 'Emergency Departments')], max_length=200, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='service/defaultea.jpg', upload_to='service')),
            ],
        ),
        migrations.DeleteModel(
            name='ExpertArea',
        ),
    ]
