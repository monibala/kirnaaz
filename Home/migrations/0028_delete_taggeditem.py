# Generated by Django 3.2.6 on 2022-02-02 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0027_taggeditem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaggedItem',
        ),
    ]