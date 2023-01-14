# Generated by Django 4.1.5 on 2023-01-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tablecount_tablegeos_tablegeov_tableskills_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(default=None, max_length=1000, verbose_name='Описание')),
                ('text1', models.TextField(default=None, verbose_name='Текст1')),
                ('title2', models.CharField(default=None, max_length=1000, verbose_name='Кто такой специалист')),
                ('text2', models.TextField(default=None, verbose_name='Текст2')),
                ('title3', models.CharField(default=None, max_length=1000, verbose_name='Обязанности')),
                ('text3', models.TextField(default=None, verbose_name='Текст3')),
                ('image', models.CharField(default=None, max_length=1000, verbose_name='Ссылка')),
            ],
        ),
        migrations.AddField(
            model_name='tablecount',
            name='count_tech',
            field=models.CharField(default='', max_length=1000, verbose_name='Количество вакансий техподдержки'),
        ),
        migrations.AddField(
            model_name='tablesalary',
            name='salary_tech',
            field=models.CharField(default='', max_length=1000, verbose_name='зарплата специалиста техподдержки'),
        ),
        migrations.AlterField(
            model_name='tablecount',
            name='count',
            field=models.CharField(default='', max_length=1000, verbose_name='Количество вакансий в IT'),
        ),
        migrations.AlterField(
            model_name='tablesalary',
            name='salary',
            field=models.CharField(default='', max_length=1000, verbose_name=' зарплата в IT'),
        ),
    ]
