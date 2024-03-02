from django.db import models

# Create your models here.
class UserData(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    # profilePicture = models.ImageField()
    userName = models.CharField(max_length=255)
    emailId = models.EmailField()
    password = models.CharField(max_length=25)


class LoginData(models.Model):
    pass
