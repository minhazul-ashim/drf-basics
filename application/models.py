from django.db import models
from django.contrib.auth.models import User;
from job.models import Job;

# Create your models here.
class Application(models.Model) :
    createdAt = models.DateTimeField(auto_now_add=True);
    job = models.ForeignKey(Job, related_name='job_application', on_delete=models.CASCADE);
    user = models.ForeignKey(User, related_name='user_application', on_delete=models.CASCADE);