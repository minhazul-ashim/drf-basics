from rest_framework import viewsets
from .models import Application;
from rest_framework import permissions
from .serializer import AppplicationSerializer;

class ApplicationViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Application.objects.all()
    serializer_class = AppplicationSerializer