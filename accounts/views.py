from rest_framework import viewsets
from .models import UserAccount;
from .serializer import AccountSerializer;

class AccountViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = UserAccount.objects.all()
    serializer_class = AccountSerializer