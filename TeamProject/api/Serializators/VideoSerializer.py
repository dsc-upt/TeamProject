from rest_framework import serializers

from api.Models.VideoModel import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['Title', 'Description', 'Url', 'Category']