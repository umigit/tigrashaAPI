from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'name', 'place', 'date', 'detail', 'address', 'latitude', 'longitude', 'image', 'created_at', 'updated_at')