from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.homeview, name='homepage'),
    path('recipes/', views.FoodieListView.as_view(), name='recipes'),
    path('recipe/<int:recipe_id>/create_rating/', views.rating, name='create_rating'),
    path('recipe/detail_recipes/<int:pk>/',views.DetailFoodiesView.as_view(),name='detail-view')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
