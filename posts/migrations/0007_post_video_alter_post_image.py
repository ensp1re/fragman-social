# Generated by Django 4.2.5 on 2023-12-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, upload_to='post_video/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images'),
        ),
    ]
