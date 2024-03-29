from rest_framework.views import APIView;
from rest_framework.response import Response
from .serializer import AuthenticationSerializer;
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login, logout;
from rest_framework.authtoken.models import Token;
from django.shortcuts import redirect;
from accounts.models import UserAccount;

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request) :
        serializer = AuthenticationSerializer(data=self.request.data);
        if serializer.is_valid() :
            username = serializer.validated_data['username'];
            password = serializer.validated_data['password'];

            user = authenticate(username=username, password=password);
            account = UserAccount.objects.get(user=user);
            if user :
                token, created = Token.objects.get_or_create(user=user);
                login(request, user);
                return Response({'token': token.key, 'userId': account.id });
            else :
                return Response({'error' : 'Invalid credentials'});

        return Response(serializer.errors);

class UserLogoutView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'User Logged out. Token deleted'})
        except AttributeError:
            pass

        logout(request)
        return Response({'message': 'User Logged out. Token deleted'})
