# Generated by Django 5.0.2 on 2024-09-07 07:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacted',
            new_name='Contact',
        ),
    ]