from rest_framework import viewsets
from .models import Job;
from rest_framework.permissions import AllowAny
from .serializer import JobSerializer;

class JobViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Job.objects.all()
    serializer_class = JobSerializer