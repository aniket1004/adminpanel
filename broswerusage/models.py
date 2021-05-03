from django.db import models

# Create your models here.
class BroswerUsage(models.Model):
    name = models.CharField(max_length=100,blank = False)
    users = models.IntegerField()