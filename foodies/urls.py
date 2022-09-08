from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview,name='homepage'),
    path('recipes/', views.FoodieListView.as_view(),name='recipes'),
    # path('search-food/', views.foodiefilterview,name='search-food'),

]