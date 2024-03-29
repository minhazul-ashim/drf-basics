from rest_framework import serializers;
from job.serializer import JobSerializer
from . import models;

class AppplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = ['id', 'createdAt', 'job', 'user']
