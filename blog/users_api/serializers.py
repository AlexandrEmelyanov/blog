from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')


# class UserSerializers(serializers.Serializer):
#     first_name = serializers.CharField(max_length=128)
#     last_name = serializers.CharField(max_length=128)
#     email = serializers.EmailField()
#     username = serializers.CharField(max_length=128)
#     image = serializers.ImageField(allow_empty_file=True, allow_null=True)
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get("first_name", instance.first_name)
#         instance.last_name = validated_data.get("last_name", instance.last_name)
#         instance.email = validated_data.get("email", instance.email)
#         instance.username = validated_data.get("username", instance.username)
#         instance.image = validated_data.get("first_name", instance.image)
#         instance.save()
#         return instance
