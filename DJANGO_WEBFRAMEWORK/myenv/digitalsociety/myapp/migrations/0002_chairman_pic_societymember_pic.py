# Generated by Django 4.2.4 on 2023-08-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='media/user-icon.jpg', upload_to='media/images'),
        ),
        migrations.AddField(
            model_name='societymember',
            name='pic',
            field=models.FileField(default='media/user-icon.jpg', upload_to='media/images'),
        ),
    ]
