# Generated by Django 3.1.3 on 2020-11-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakes', '0014_snakecard_create_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='snakecard',
            name='some_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
