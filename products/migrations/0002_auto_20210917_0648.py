# Generated by Django 3.2.7 on 2021-09-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_unit',
            field=models.IntegerField(choices=[(1, 'kg'), (2, 'gm'), (3, 'ltr'), (4, 'ml'), (5, 'unit')], default=1),
            preserve_default=False,
        ),
    ]
