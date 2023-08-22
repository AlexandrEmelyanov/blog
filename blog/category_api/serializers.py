from rest_framework import serializers

from site_blog.models import PostCategory


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = '__all__'
