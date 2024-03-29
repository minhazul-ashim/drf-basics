from django.db import models
from django.contrib.auth.models import User;

# Create your models here.
class UserAccount(models.Model) :
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE);
    accType = models.CharField(max_length = 10);
    location = models.CharField(max_length = 100, null=True);
    phone = models.CharField(max_length = 20, null=True);
    upload = models.FileField(upload_to="uploads/", null=True, blank=True)
    