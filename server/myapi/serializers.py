from rest_framework import serializers

from .models import Post


# class HeroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Hero
#         fields = ('name', 'alias')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image')
