# Generated by Django 5.0.2 on 2024-02-14 20:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(upload_to='job_images/')),
                ('email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('job_region', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('company_name', models.CharField(max_length=100)),
                ('tagline', models.CharField(blank=True, max_length=100, null=True)),
                ('company_description', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('facebook_username', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter_username', models.CharField(blank=True, max_length=50, null=True)),
                ('linkedin_username', models.CharField(blank=True, max_length=50, null=True)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
            ],
            options={
                'db_table': 'JobPosting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('message', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
