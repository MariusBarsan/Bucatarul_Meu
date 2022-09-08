import requests
from django.http import HttpResponse
from django.shortcuts import render

from foodies.models import Recipe


def index(request):
    # context = Recipe.objects.all().count()
    response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood")
    jsonResponse = response.json()
    meals = jsonResponse['meals']
    return render(request, 'MainPage/index.html', {'meals':meals})
    # context = {'count_all_recipes': context}

def specific(request):
    return HttpResponse("This is the specific url")

def singleMeal(request):
    mealId = request.GET.get('mealId')
    response = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i='+str(mealId))
    jsonResponse = response.json()
    meals = jsonResponse['meals']
    return render(request, 'MainPage/single_meal.html', {'meals':meals})
