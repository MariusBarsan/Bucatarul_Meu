# Generated by Django 4.0.2 on 2022-09-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganduri', '0006_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
