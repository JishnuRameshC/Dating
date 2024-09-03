# Generated by Django 4.2.5 on 2024-09-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_jobprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobprofile',
            old_name='designation',
            new_name='job_title',
        ),
        migrations.RemoveField(
            model_name='jobprofile',
            name='title',
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='experience',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='salary',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=25),
        ),
    ]
