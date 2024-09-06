# Generated by Django 5.0.3 on 2024-09-04 08:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_address_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='additional_images',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='drinking_habits',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='qualifications',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='short_reel',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='smoking_habits',
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_status', models.CharField(choices=[('employer', 'Employer'), ('employee', 'Employee'), ('job_seeker', 'Job Seeker')], max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('job_title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('expertise_level', models.CharField(blank=True, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')], max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=25)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('religion', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('hobbies', models.CharField(blank=True, default='', max_length=255)),
                ('interests', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Both')], default='', max_length=25)),
                ('smoking_habits', models.CharField(blank=True, choices=[('N', 'Never'), ('O', 'Occasionally'), ('F', 'Frequently')], default='', max_length=25)),
                ('drinking_habits', models.CharField(blank=True, choices=[('N', 'Never'), ('O', 'Occasionally'), ('F', 'Frequently')], default='', max_length=25)),
                ('qualifications', models.CharField(blank=True, choices=[('SSLC', 'SSLC'), ('+2', 'Plus Two'), ('diploma', 'Diploma'), ('degree', 'Degree'), ('PG', 'Postgraduate'), ('PHD', 'PhD')], default='', max_length=25)),
                ('profile_pic', models.ImageField(blank=True, default='', null=True, upload_to='profile_pics/')),
                ('short_reel', models.FileField(blank=True, default='', null=True, upload_to='short_reels/')),
                ('relationship_goals', models.CharField(blank=True, choices=[('long_term', 'short_term'), ('short_term', 'short_term')], default='', max_length=25, null=True)),
                ('additional_images', models.ManyToManyField(blank=True, to='accounts.additionalimage')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]