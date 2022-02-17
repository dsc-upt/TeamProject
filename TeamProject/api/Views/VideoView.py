from requests import Response
from rest_framework.decorators import api_view

from api.Models.VideoModel import Video
from api.Serializators.VideoSerializer import VideoSerializer


@api_view(['GET', 'POST'])
def videos_list(request):
    if request.method == "GET":
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    # elif request.method == "POST":
    #     if CustomUser.objects.filter(username=request.data['username']).exists():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     serializer = CustomUserSerializerPassword(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)