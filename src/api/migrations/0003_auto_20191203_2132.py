# Generated by Django 2.2.7 on 2019-12-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191203_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='image_url',
            field=models.URLField(default=None, max_length=2500),
        ),
        migrations.AddField(
            model_name='anime',
            name='thumbnail_url',
            field=models.URLField(default=None, max_length=2500),
        ),
    ]
