# Generated by Django 2.2 on 2019-10-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190518_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='cart',
            name='neighbourhood',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='neighbourhood'),
        ),
        migrations.AddField(
            model_name='cart',
            name='payment_status',
            field=models.BooleanField(default=False, verbose_name='payment status'),
        ),
        migrations.AddField(
            model_name='cart',
            name='region',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='region'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
    ]