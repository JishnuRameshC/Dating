# Generated by Django 4.2.5 on 2024-09-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_customuser_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_status', models.CharField(choices=[('employer', 'Employer'), ('employee', 'Employee'), ('job_seeker', 'Job Seeker')], max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('expertise_level', models.CharField(blank=True, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')], max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='qualifications',
            field=models.CharField(blank=True, choices=[('SSLC', 'SSLC'), ('+2', 'Plus Two'), ('diploma', 'Diploma'), ('degree', 'Degree'), ('PG', 'Postgraduate'), ('PHD', 'PhD')], default='', max_length=255),
        ),
    ]
