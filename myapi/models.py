from django.db import models

# Create your models here.


class users(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    weight = models.IntegerField()
    password = models.CharField(max_length=50)
    sessionId = models.CharField(max_length=100)
