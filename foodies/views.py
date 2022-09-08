from functools import reduce

from django.shortcuts import render
from django.views.generic import ListView
from foodies.models import Recipe
from django.db.models import Q
from django.shortcuts import render


def homeview(request):

    return render(request, 'MainPage/index.html')


class FoodieListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'foodies/search_foodies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        keywords = self.request.GET['keywords'].split()
        topics = list(self.request.GET.keys())
        topics.remove('keywords')
        print('zzzz', self.request.GET)
        filter_keywords_query = Q()
        for keyword in keywords:
            filter_keywords_query |= Q(title__icontains=keyword)
        filter_topics_query = Q()
        for topic in topics:
            filter_topics_query |= Q(topic__title__icontains=topic)

        recipes = self.get_queryset().filter(filter_keywords_query&filter_topics_query)
        context['recipes'] = recipes

        return context
