from django.db import models


class Index(models.Model):
    title1 = models.CharField('Описание', max_length=1000, default='1214141')
    text1 = models.TextField('Текст1', default=None)
    title2 = models.CharField('Кто такой специалист', max_length=1000, default=None)
    text2 = models.TextField('Текст2', default=None)
    title3 = models.CharField('Обязанности', max_length=1000, default=None)
    text3 = models.TextField('Текст3', default=None)
    image = models.CharField('Ссылка', max_length=1000, default = None)

class TableSalary(models.Model):
    year = models.CharField('Год', max_length=4, default='')
    salary = models.CharField(' зарплата в IT', max_length=1000, default='')
    salary_tech = models.CharField('зарплата специалиста техподдержки', max_length=1000, default='')

    def __str__(self):
        return self.year


class TableCount(models.Model):
    year = models.CharField('Год', max_length=4, default='')
    count = models.CharField('Количество вакансий в IT', max_length=1000, default='')
    count_tech = models.CharField('Количество вакансий техподдержки', max_length=1000, default='')

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
