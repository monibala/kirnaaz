# Generated by Django 3.2 on 2021-08-10 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxfiling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxfiling',
            name='slug',
        ),
    ]
