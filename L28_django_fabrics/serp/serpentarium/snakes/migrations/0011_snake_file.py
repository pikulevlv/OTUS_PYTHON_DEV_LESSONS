# Generated by Django 3.1.3 on 2020-11-15 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakes', '0010_specia_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='snake',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='snake_examples'),
        ),
    ]
