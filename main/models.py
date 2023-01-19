from codecs import charmap_build
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class files(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    fileinput = models.CharField(max_length=20000000)
    txt = models.TextField(max_length=100000000000000000000000000000000000000000000, default="")

    def __str__(self) -> str:
        return self.name

