# Generated by Django 4.2.5 on 2023-11-14 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_like_post_liked_delete_likepost_like_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='liked',
            new_name='liked_by',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
