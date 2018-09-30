from rest_framework import serializers, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import News
from apps.topics.views import TopicsSerializer

import json
from datetime import datetime
from django.template import loader

from django.shortcuts import render, HttpResponse

# serializers
class NewsSerializer(serializers.ModelSerializer):
    # topics = TopicsSerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'status', 'topics', )


# views API
class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('status', 'topics', )
    permission_classes = (AllowAny,)


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)


@api_view(['DELETE'])
@permission_classes((AllowAny, ))
def delete_status_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.status = 'deleted'
    news.save()
    return Response({"message": "news deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes((AllowAny, ))
def delete_data_news(request, pk):
    # if not request.user.is_superuser:
    #     return Response({"message": "not allowed"}, status=status.HTTP_403_FORBIDDEN)
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return Response({"message": "news deleted"}, status=status.HTTP_204_NO_CONTENT)
