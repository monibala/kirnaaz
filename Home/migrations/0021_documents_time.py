# Generated by Django 3.2 on 2021-08-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0020_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
