from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length = 20,blank=False)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)