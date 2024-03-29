from rest_framework import viewsets
from .models import Application;
from .serializer import AppplicationSerializer;

class ApplicationViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Application.objects.all()
    serializer_class = AppplicationSerializer