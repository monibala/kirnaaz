# Generated by Django 3.2.6 on 2022-02-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0040_blognews'),
    ]

    operations = [
        migrations.AddField(
            model_name='blognews',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]