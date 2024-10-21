# Generated by Django 4.2.8 on 2024-10-21 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='research/'),
        ),
        migrations.AddField(
            model_name='research',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='research/'),
        ),
    ]
