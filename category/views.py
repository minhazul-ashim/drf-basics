from rest_framework import viewsets
from .models import Category;
from .serializer import CategorySerializer;

class CategoryViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer