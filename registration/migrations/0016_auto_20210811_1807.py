# Generated by Django 3.2 on 2021-08-11 12:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_alter_sainification_content2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutregistraionsubmenu',
            name='heading1_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutregistraionsubmenu',
            name='heading2_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]