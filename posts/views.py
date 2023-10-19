from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from posts.serializer import PostSerializer, PostTopicSerializer


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'text']
    filterset_fields = ['post_topic']
    # ordering_fields = ['id']
    # permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     queryset = Post.objects.all()
    # #
    #     params = self.request.query_params
    #
    #     post_topic = params.get('post_topic', None)
    #
    #     if post_topic:
    #         queryset = queryset.filter(post_topic=post_topic)
    # #
    #     return queryset


class PostTopicListView(generics.ListAPIView):
    queryset = PostTopic.objects.all()
    serializer_class = PostTopicSerializer
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['title', 'text']
