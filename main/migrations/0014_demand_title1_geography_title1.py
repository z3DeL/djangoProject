# Generated by Django 4.1.5 on 2023-01-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_demand_title1_remove_geography_title1'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='title1',
            field=models.CharField(default=None, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='geography',
            name='title1',
            field=models.CharField(default=None, max_length=1000, null=True, verbose_name='Описание'),
        ),
    ]
