# Generated by Django 5.0.3 on 2024-08-30 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_additionalimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='location',
        ),
    ]
