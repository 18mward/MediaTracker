# Generated by Django 3.1.2 on 2020-10-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_card_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='seasons',
            field=models.CharField(default='N/A', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='stream_sites',
            field=models.TextField(default='None currently available.'),
            preserve_default=False,
        ),
    ]
