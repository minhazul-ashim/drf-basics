from rest_framework import serializers;
from . import models;
from django.contrib.auth.models import User;
from rest_framework import serializers
from application.serializer import AppplicationSerializer;
from job.serializer import JobSerializer;
from .models import UserAccount

class UserSerializer(serializers.ModelSerializer):
    user_posted_job = JobSerializer(many=True)
    user_application = AppplicationSerializer(many=True) 
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'user_posted_job', 'user_application']

    def get_user_posted_job(self, obj):
        posted_jobs = obj.user_posted_job.all()
        return JobSerializer(posted_jobs, many=True).data

    def get_user_application(self, obj):
        applied_jobs = obj.user_application.all()
        return JobSerializer(applied_jobs, many=True).data

class UserAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserAccount
        fields = ['user', 'accType', 'location', 'phone', 'resume']

class AccountSerializer(serializers.ModelSerializer) :
    confirm_pass = serializers.CharField(required=True);
    accType = serializers.CharField();
    location = serializers.CharField();
    phone = serializers.CharField();
    class Meta :
        model = User;
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_pass', 'accType', 'location', 'phone'];

    def save(self) :
        username = self.validated_data['username'];
        email = self.validated_data['email'];
        first_name = self.validated_data['first_name'];
        last_name = self.validated_data['last_name'];
        accType = self.validated_data['accType'];
        location = self.validated_data['location'];
        phone = self.validated_data['phone'];
        password = self.validated_data['password'];
        password2 = self.validated_data['confirm_pass'];

        if password != password2 :
            raise serializers.ValidationError({'error': 'Passwords do not match'});

        if User.objects.filter(email=email).exists() :
            raise serializers.ValidationError({'error': 'Email already exists'});

        account = User(username=username, email=email, first_name=first_name, last_name=last_name);
        account.set_password(password)
        account.save();

        useraccount = models.UserAccount(user=account, accType=accType, location=location, phone=phone);
        useraccount.save();


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAccount

class AccountUpdateSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    accType = serializers.CharField()
    location = serializers.CharField()
    phone = serializers.CharField()
    resume = serializers.FileField(required=False)

    def save(self, request):
        username = self.validated_data['username']
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        accType = self.validated_data['accType']
        location = self.validated_data['location']
        phone = self.validated_data['phone']
        
        user = request.user

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        user_account = UserAccount.objects.get(user=user)

        user_account.accType = accType
        user_account.location = location
        user_account.phone = phone

        if 'resume' in self.validated_data:
            resume = self.validated_data['resume']
            user_account.resume = resume

        user_account.save()

