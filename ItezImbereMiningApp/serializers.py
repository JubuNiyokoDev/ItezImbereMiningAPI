from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Users,UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        Token.objects.create(user=user)  # Création d'un token pour l'utilisateur
        return user

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'country')

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.country = validated_data.get('country', instance.country)

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'phone_number', 'address', 'profile_picture')