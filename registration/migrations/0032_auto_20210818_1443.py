# Generated by Django 3.2 on 2021-08-18 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0031_rename_image_procedure_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packageincluded',
            name='image',
        ),
        migrations.AddField(
            model_name='packageincluded',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.icon'),
        ),
    ]
