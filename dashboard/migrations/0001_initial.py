# Generated by Django 3.2 on 2021-08-13 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0021_alter_procedure_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(default='["Included in Our Packge","Procedure","document","Memorandum","Register","FAQS","Signification"]', max_length=1000)),
                ('reg_title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.registrationsubmenu')),
            ],
        ),
    ]
