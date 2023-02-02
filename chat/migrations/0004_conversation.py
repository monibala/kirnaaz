# Generated by Django 3.1.7 on 2021-06-17 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210617_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now=True)),
                ('msgby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgby', to='chat.user')),
                ('msgto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgto', to='chat.user')),
            ],
        ),
    ]
