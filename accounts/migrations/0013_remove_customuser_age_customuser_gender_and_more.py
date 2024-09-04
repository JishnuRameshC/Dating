# Generated by Django 4.2.5 on 2024-08-30 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_additionalimage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='drinking_habits',
            field=models.CharField(blank=True, choices=[('N', 'Never'), ('O', 'Occasionally'), ('F', 'Frequently')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='interests',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Both')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='smoking_habits',
            field=models.CharField(blank=True, choices=[('N', 'Never'), ('O', 'Occasionally'), ('F', 'Frequently')], default='', max_length=50),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address_line_1', models.CharField(max_length=250)),
                ('address_line_2', models.CharField(max_length=250)),
                ('address_line_3', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=100)),
                ('is_default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
    ]