# Generated by Django 5.0.3 on 2024-10-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_personaldetails_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pics/'),
        ),
    ]