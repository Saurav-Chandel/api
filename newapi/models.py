from django.db import models

# Create your models here.
class Hero(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254,null=True,unique=True)


def __str__(self):
       return self.name    
