# Generated by Django 3.2 on 2021-08-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('othernavs', '0004_auto_20210814_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='subregistrationcontent',
            name='formtitle',
            field=models.CharField(default='title', max_length=500),
            preserve_default=False,
        ),
    ]