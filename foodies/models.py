from django.db import models
from autoslug import AutoSlugField

from userextend.models import UserExtend


class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title",max_length=200)

    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title",max_length=200)
    image = models.ImageField(upload_to='media/',null=True,blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    servings = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    calories = models.CharField(max_length=5)
    fat = models.CharField(max_length=5)
    carbs = models.CharField(max_length=5)
    protein = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user = models.ForeignKey(UserExtend,on_delete=models.CASCADE)
    number = models.IntegerField()
