from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import PostTopic, Post
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']


class PostTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTopic
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post_topic = PostTopicSerializer()

    class Meta:
        model = Post
        fields = '__all__'
