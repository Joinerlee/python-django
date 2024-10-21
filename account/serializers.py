from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # Dynamically get the user model

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        if validated_data.get('is_superuser'):
            user.is_superuser = True
            user.is_staff = True
            user.save()
        return user
