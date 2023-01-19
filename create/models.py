from django.db import models

# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class forgot(models.Model):
    email = models.CharField(max_length=200)
    friend_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.email

