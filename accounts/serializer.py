from rest_framework import serializers;
from . import models;
from django.contrib.auth.models import User;

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


class AccountUpdateSerializer(serializers.ModelSerializer) :
    confirm_pass = serializers.CharField(required=True);
    accType = serializers.CharField();
    location = serializers.CharField();
    phone = serializers.CharField();
    resume = serializers.FileField(required=False);
    class Meta :
        model = models.UserAccount;
        fields = ['username', 'first_name', 'last_name', 'email', 'accType', 'location', 'phone', 'resume'];

    def save(self) :
        username = self.validated_data['username'];
        email = self.validated_data['email'];
        first_name = self.validated_data['first_name'];
        last_name = self.validated_data['last_name'];
        accType = self.validated_data['accType'];
        location = self.validated_data['location'];
        phone = self.validated_data['phone'];

        user = User.objects.filter(username=username);

        user.update(username=username, first_name=first_name, last_name=last_name, email=email);

        useraccount = models.UserAccount.objects.filter(user=user);

        if self.validated_data['resume'] :
            resume = self.validated_data['resume']
            useraccount.update(resume=resume);

        useraccount.update(accType=accType, location=location, phone=phone)

