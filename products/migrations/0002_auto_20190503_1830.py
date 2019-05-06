# Generated by Django 2.2 on 2019-05-03 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.TextField(help_text='Comma seperated list of available sizes', validators=[django.core.validators.RegexValidator('^(\\d+,)*\\d+$')], verbose_name='size'),
        ),
    ]