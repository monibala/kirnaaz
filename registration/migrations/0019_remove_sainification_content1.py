# Generated by Django 3.2 on 2021-08-12 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20210812_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sainification',
            name='content1',
        ),
    ]
