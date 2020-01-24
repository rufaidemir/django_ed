# Generated by Django 3.0.2 on 2020-01-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_auto_20200124_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courusel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('cover_image', models.ImageField(blank=True, upload_to='couresel')),
                ('status', models.TextField(choices=[('draft', 'taslak'), ('published', 'yayinlandi'), ('deleted', 'silindi')], default='draft')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.TextField(choices=[('draft', 'taslak'), ('published', 'yayinlandi'), ('deleted', 'silindi')], default='draft'),
        ),
    ]
