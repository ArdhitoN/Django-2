# Generated by Django 4.1 on 2022-09-19 15:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0004_alter_mywatchlist_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
