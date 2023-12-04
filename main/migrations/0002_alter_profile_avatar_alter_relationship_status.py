# Generated by Django 4.2.5 on 2023-10-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='photo_2021-10-16_13-01-08.jpg', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('accepted', 'accepted')], max_length=8),
        ),
    ]