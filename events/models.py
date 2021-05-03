from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100,blank=False,)
    slug = models.CharField(max_length=100,blank=False,)
    date = models.DateField(auto_now=False, auto_now_add=False)
    