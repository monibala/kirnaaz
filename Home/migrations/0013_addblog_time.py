# Generated by Django 3.2 on 2021-08-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_addblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='addblog',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
