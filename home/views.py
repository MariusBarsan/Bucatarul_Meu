from django.views.generic import TemplateView
import requests
from django.http import HttpResponse
from django.shortcuts import render


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'


def index(request):
    response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood")
    jsonResponse = response.json()
    meals = jsonResponse['meals']
    return render(request, 'home/home.html', {'meals': meals})


def specific(request):
    return HttpResponse("This is the specific url")


def singleMeal(request):
    mealId = request.GET.get('mealId')
    response = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i=' + str(mealId))
    jsonResponse = response.json()
    meals = jsonResponse['meals']
    return render(request, 'home/single_meal1.html', {'meals': meals})
