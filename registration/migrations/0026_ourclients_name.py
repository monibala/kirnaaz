# Generated by Django 3.2 on 2021-08-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0025_ourclients_signatureoptional'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourclients',
            name='name',
            field=models.CharField(default='Praveen Chouhan', max_length=30),
            preserve_default=False,
        ),
    ]