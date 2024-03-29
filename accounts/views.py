from rest_framework import viewsets
from .models import UserAccount;
from .serializer import AccountSerializer, AccountUpdateSerializer
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework import status

class AccountViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = AccountSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(APIView):
    serializer_class = AccountUpdateSerializer
    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)