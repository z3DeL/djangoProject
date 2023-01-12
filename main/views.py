from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def demand(request):
    table_salary = TableSalary.objects.all()
    table_count = TableCount
    return render(request, 'main/demand.html', {'salary': table_salary, 'count': table_count})


def geography(request):
    table_salary = TableGeoS.objects.all()
    table_count = TableGeoV.objects.all()
    return render(request, 'main/geography.html', {'salary': table_salary, 'count': table_count})


def last_vacancies(request):
    return render(request, 'main/last_vacancies.html')


def skills(request):
    table_skills = TableSkills.objects.all()
    return render(request, 'main/skills.html', {'skills': table_skills})
