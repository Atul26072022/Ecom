from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)



