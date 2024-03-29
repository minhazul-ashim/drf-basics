from rest_framework import serializers;
from django.contrib.auth import login, logout, authenticate;

class AuthenticationSerializer(serializers.Serializer) :
    username = serializers.CharField(required=True);
    password = serializers.CharField(required=True);

    class Meta :
        fields = ['username', 'password'];
        