# Generated by Django 3.1.3 on 2020-11-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakes', '0011_snake_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snake',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
