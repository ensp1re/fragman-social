# Generated by Django 4.2.5 on 2023-11-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_relationship_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.UUIDField(default='3857055833-2110733303', primary_key=True, serialize=False),
        ),
    ]
