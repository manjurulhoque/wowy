# Generated by Django 3.2.7 on 2021-09-17 06:17

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Product name')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=products.models.product_image_directory_path)),
                ('fake_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, max_length=40, null=True)),
                ('stock', models.IntegerField()),
                ('stock_unit', models.IntegerField(choices=[(1, 'kg'), (2, 'gm'), (3, 'ltr'), (4, 'ml'), (5, 'unit')])),
                ('top_featured', models.BooleanField(default=False)),
                ('detail', models.TextField()),
                ('detail_desc', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
