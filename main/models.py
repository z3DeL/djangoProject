from django.db import models


class TableSalary(models.Model):
    year = models.CharField('Год', max_length=4, default='')
    salary = models.CharField('зарплата специалиста техподдержки', max_length=1000, default='')

    def __str__(self):
        return self.year


class TableCount(models.Model):
    year = models.CharField('Год', max_length=4, default='')
    count = models.CharField('Количество вакансий', max_length=1000, default='')

    def __str__(self):
        return self.year


class TableGeoS(models.Model):
    city = models.TextField('Город', default='')
    salary = models.CharField('Зарплаты', max_length=1000, default='')

    def __str__(self):
        return self.city


class TableGeoV(models.Model):
    city = models.TextField('Город', default='')
    perc = models.CharField('Доля вакансий в %', max_length=1000, default='')

    def __str__(self):
        return self.city


class TableSkills(models.Model):
    year = models.CharField('Год',max_length=4, default='')
    skills = models.TextField('Топ 10 навыков', default='')

    def __str__(self):
        return self.year
