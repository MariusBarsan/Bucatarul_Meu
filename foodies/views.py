from functools import reduce

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from foodies.forms import RatingForm
from foodies.models import Recipe, Rating
from django.db.models import Q, Sum
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView

from userextend.models import UserExtend


def homeview(request):
    return render(request, 'MainPage/index.html')


class FoodieListView(ListView, LoginRequiredMixin):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'foodies/search_foodies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'keywords' in self.request.GET:
            keywords = self.request.GET['keywords'].split()
        else:
            keywords = []
        topics = list(self.request.GET.keys())
        if 'keywords' in topics:
            topics.remove('keywords')
        filter_keywords_query = Q()
        for keyword in keywords:
            filter_keywords_query |= Q(title__icontains=keyword)
        filter_topics_query = Q()
        for topic in topics:
            filter_topics_query |= Q(topic__title__icontains=topic)

        recipes = self.get_queryset().filter(filter_keywords_query & filter_topics_query)
        context['recipes'] = recipes
        context['rating_form'] = RatingForm()

        return context


class CreateRatingView(CreateView, LoginRequiredMixin):
    form_class = RatingForm
    model = Rating
    success_url = reverse_lazy('index')
    template_name = 'foodies/create_rating.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'initial': {'user': self.request.user.id, 'recipe': self.kwargs.get('pk')}})
        return kwargs


class DetailFoodiesView(DetailView, LoginRequiredMixin):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'foodies/detail_foodies.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        ratings = self.object.rating_set.aggregate(Sum('number')).get('number__sum')  # sum of ratings
        if not ratings:
            average_rating = 0
        else:
            average_rating = ratings / self.object.rating_set.count()
        data['average_rating'] = average_rating
        has_rated = Rating.objects.filter(user__id=self.request.user.id, recipe=self.object).count() >= 1
        data['has_rated'] = has_rated

        return data


@login_required
def rating(request, recipe_id):
    rating_number = int(request.POST.get('number'))
    if 0 <= rating_number <= 5:
        Rating.objects.create(recipe=Recipe.objects.get(id=recipe_id), user=UserExtend.objects.get(id=request.user.id),
                              number=rating_number)
    return redirect('detail-view', pk=recipe_id)
