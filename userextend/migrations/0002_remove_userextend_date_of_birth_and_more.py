# Generated by Django 4.0.2 on 2022-08-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userextend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextend',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='userextend',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
    ]
