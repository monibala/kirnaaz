# Generated by Django 3.2 on 2021-08-11 11:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_alter_faq_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sainification',
            name='content2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]