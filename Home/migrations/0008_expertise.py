# Generated by Django 3.2 on 2021-08-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20210816_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='imgaes')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]