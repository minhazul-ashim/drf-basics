from rest_framework import viewsets
from .models import UserAccount;
from .serializer import AccountSerializer
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

# class UserRegisterView(APIView):
#     serializer_class = RegistrationSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)