from rest_framework import serializers

from site_blog.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_com = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Comment
        fields = '__all__'
