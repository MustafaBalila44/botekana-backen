# Generated by Django 2.2 on 2019-05-18 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190506_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_items', related_query_name='wishlist_items', to='products.Product', verbose_name='product'),
        ),
    ]
