# Generated by Django 3.2 on 2021-08-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_merge_20210810_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='subregistrationcontent',
            old_name='tag_content',
            new_name='heading1',
        ),
        migrations.AddField(
            model_name='subregistrationcontent',
            name='heading1ans',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subregistrationcontent',
            name='heading2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subregistrationcontent',
            name='heading2ans',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subregistrationcontent',
            name='heading3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subregistrationcontent',
            name='heading3ans',
            field=models.TextField(blank=True, null=True),
        ),
    ]
