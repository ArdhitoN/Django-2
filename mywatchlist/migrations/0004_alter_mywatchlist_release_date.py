# Generated by Django 4.1 on 2022-09-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_rename_relase_date_mywatchlist_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='release_date',
            field=models.DateField(),
        ),
    ]