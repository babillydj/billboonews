from django.shortcuts import render
from rest_framework import serializers, generics
from rest_framework.permissions import AllowAny

from .models import Topics


# serializers
class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ('id', 'title', )


# views API
class TopicsList(generics.ListCreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer
    permission_classes = (AllowAny,)


class TopicsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer
    permission_classes = (AllowAny,)