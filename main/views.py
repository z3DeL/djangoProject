from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    page = Index.objects.all()[0]
    return render(request, "main/index.html", context={'mainpage': page})


def demand(request):
    table_salary = TableSalary.objects.all()
    table_count = TableCount.objects.all()
    page = Demand.objects.all()[0]
    return render(request, "main/demand.html", {'table_salary': table_salary, 'table_count': table_count, 'page': page})


def geography(request):
    table_salary = TableGeoS.objects.all()
    table_count = TableGeoV.objects.all()
    page = Geography.objects.all()[0]
    return render(request, 'main/geography.html', {'table_salary': table_salary, 'table_count': table_count, 'page': page})


def last_vacancies(request):
    return render(request, 'main/last_vacancies.html')


def skills(request):
    table_skills = TableSkills.objects.all()
    page = Skills.objects.all()[0]
    return render(request, 'main/skills.html', {'table_skills': table_skills,'page':page})


