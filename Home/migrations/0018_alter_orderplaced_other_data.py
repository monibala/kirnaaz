# Generated by Django 3.2 on 2021-08-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_orderplaced_other_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='other_data',
            field=models.CharField(default='nodata', max_length=1000),
        ),
    ]
