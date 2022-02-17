from rest_framework import serializers

from TeamProject.api.Models.VideoModel import Category


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['Name']