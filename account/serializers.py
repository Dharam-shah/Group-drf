from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'groups', 'user_permissions']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email',  'groups', 'user_permissions', 'password', 'password2')

    minimum_length = 5
    password = serializers.CharField(
        write_only=True,
        min_length = minimum_length,
        error_messages={
            "min_length": f"password must be longer than { minimum_length} characters"
        }
    )

    password2 = serializers.CharField(
        write_only=True,
        min_length = minimum_length,
        error_messages={
            "min_length": f"password must be longer than { minimum_length} characters"
        }
    )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("password does not match")

        return data

    def create(self, validate_data):
        user_obj = User.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            first_name = validate_data['first_name'],
            last_name = validate_data['last_name'],
        )
    
        user_obj.set_password(validate_data['password'])
        user_obj.save()

        return user_obj