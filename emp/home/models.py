from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.PositiveIntegerField()
    designation = models.CharField(max_length=30)
    address = models.CharField(max_length=150)