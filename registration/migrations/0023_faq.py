# Generated by Django 3.2 on 2021-08-14 07:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_delete_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=500, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('reg_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.registrationsubmenu')),
            ],
        ),
    ]
