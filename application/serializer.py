from rest_framework import serializers;
from . import models;

class AppplicationSerializer(serializers.ModelSerializer) :
    class Meta :
        model = models.Application;
        fields = "__all__";
