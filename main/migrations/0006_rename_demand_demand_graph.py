# Generated by Django 4.1.5 on 2023-01-13 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_demand_alter_index_title1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Demand',
            new_name='Demand_graph',
        ),
    ]
