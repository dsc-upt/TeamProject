from django.db import models

from api.Models.CategoryModel import Category

class Video(models.Model):
    Title=models.CharField
    Description=models.TextField
    Url=models.URLField
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

