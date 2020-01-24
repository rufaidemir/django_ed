# Generated by Django 3.0.2 on 2020-01-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20200124_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(upload_to='page'),
        ),
    ]
