from django.db import models

# Create your models here.

class Userinfo(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
