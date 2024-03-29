from rest_framework import viewsets
from .models import Job;
from .serializer import JobSerializer;

class JobViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer