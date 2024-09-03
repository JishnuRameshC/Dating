# Generated by Django 5.1 on 2024-08-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_customuser_gender'),
    ]

    operations = [
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