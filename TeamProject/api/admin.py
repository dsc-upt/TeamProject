from django.contrib import admin

from api.Models.VideoModel import Video
from api.Models.CategoryModel import Category


admin.site.register(Video)
admin.site.register(Category)

