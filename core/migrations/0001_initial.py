# Generated by Django 5.0.7 on 2024-08-05 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(default='default.jpg', upload_to='feature_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('day', models.DateField()),
                ('time_period', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=2)),
                ('doctor_name', models.CharField(choices=[('Dr. Smith', 'Dr. Smith'), ('Dr. Johnson', 'Dr. Johnson'), ('Dr. Williams', 'Dr. Williams')], default='Dr. Smith', max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClinicTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timetables', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('designation', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='team_pics')),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(default='defaultlogo.jpg', upload_to='home_pics')),
                ('image', models.ImageField(upload_to='home_pics')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('time', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlanService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('logo', models.ImageField(default='default.jpg', upload_to='planservice_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('logo', models.ImageField(default='default.jpg', upload_to='service_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('client_name', models.CharField(max_length=120)),
                ('profession', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.jpg', upload_to='testimonial_pics')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('day', models.CharField(max_length=10)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='about_pics')),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='core.aboutfeature')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinictimes', to='core.clinictime')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('time_duration', models.CharField(choices=[('MONTH', 'Month'), ('YEAR', 'Year'), ('ONE-TIME', 'One-Time')], default='MONTH', max_length=15)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='core.planservice')),
            ],
        ),
    ]
