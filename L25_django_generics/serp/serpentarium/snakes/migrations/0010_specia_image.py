# Generated by Django 3.1.3 on 2020-11-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakes', '0009_auto_20201107_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='specia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='kind'),
        ),
    ]
