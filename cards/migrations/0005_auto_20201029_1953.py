# Generated by Django 3.1.2 on 2020-10-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20201016_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='mediatype',
            field=models.CharField(default='all media', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='rating',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='card',
            name='seasons',
            field=models.CharField(max_length=255),
        ),
    ]
