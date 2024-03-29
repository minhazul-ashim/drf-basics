from .serializer import AccountSerializer, AccountUpdateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework import status
from accounts.models import UserAccount
from accounts.serializer import UserAccountSerializer

class AccountCreationView(APIView):
    permission_classes = [AllowAny]
    serializer_class = AccountSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(APIView):
    serializer_class = AccountUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_account = UserAccount.objects.get(user=request.user)
        serializer = UserAccountSerializer(user_account)
        return Response(serializer.data)