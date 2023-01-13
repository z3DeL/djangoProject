# Generated by Django 4.1.5 on 2023-01-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_index_title1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph1', models.CharField(default=None, max_length=1000, verbose_name='график 1')),
                ('graph2', models.CharField(default=None, max_length=1000, verbose_name='график 2')),
            ],
        ),
        migrations.AlterField(
            model_name='index',
            name='title1',
            field=models.CharField(default=None, max_length=1000, verbose_name='Описание'),
        ),
    ]