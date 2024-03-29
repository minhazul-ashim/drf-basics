from django.db import models
from category.models import Category;
from django.contrib.auth.models import User;

# Create your models here.
class Job(models.Model) :
    title = models.CharField(max_length=100);
    description = models.CharField(max_length=2500);
    location= models.CharField(max_length=30);
    company = models.CharField(max_length=30);
    jobType = models.CharField(max_length=30);
    postedAt = models.DateTimeField(auto_now_add=True);
    category = models.ForeignKey(Category, related_name='job_category', on_delete=models.CASCADE);
    postedBy = models.ForeignKey(User, related_name='user_posted_job', on_delete=models.CASCADE);

    class Meta :
        ordering = ['postedAt'];