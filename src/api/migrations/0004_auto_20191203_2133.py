# Generated by Django 2.2.7 on 2019-12-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191203_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image_url',
            field=models.URLField(default='', max_length=2500),
        ),
        migrations.AlterField(
            model_name='anime',
            name='thumbnail_url',
            field=models.URLField(default='', max_length=2500),
        ),
    ]
