from rest_framework import serializers;
from . import models;
from category.serializer import CategorySerializer;

class JobSerializer(serializers.ModelSerializer) :
    class Meta :
        model = models.Job;
        fields = "__all__";
