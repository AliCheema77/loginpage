from django.db import models

# Create your models here.

class NewUser(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
