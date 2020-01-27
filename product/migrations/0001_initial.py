# Generated by Django 3.0.2 on 2020-01-27 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(default='', max_length=175)),
                ('status', models.TextField(choices=[('draft', 'taslak'), ('published', 'yayinlandi'), ('deleted', 'silindi')], default='draft')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('slug', models.SlugField(default='', max_length=175)),
                ('cover_image', models.ImageField(blank=True, upload_to='product')),
                ('price', models.FloatField()),
                ('stock', models.PositiveSmallIntegerField()),
                ('status', models.TextField(choices=[('draft', 'taslak'), ('published', 'yayinlandi'), ('deleted', 'silindi')], default='draft')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
    ]
