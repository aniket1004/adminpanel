from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100,blank=False)
    start = models.DateField(auto_now=False,auto_now_add=False)
    end = models.DateField(auto_now=False,auto_now_add=False)
    status = models.CharField(max_length = 50,blank = False)
    assignee = models.CharField(max_length=100,blank=False)