from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    address = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'address')
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, attrs):
        email = attrs.get('email', '')
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email is already in use')})
        return super(CustomUserSerializer, self).validate(attrs)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


