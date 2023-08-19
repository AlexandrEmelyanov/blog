from rest_framework import serializers
from site_blog.models import Posts
from users.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())  # current user in hidden field

    class Meta:
        model = Posts
        fields = '__all__'



