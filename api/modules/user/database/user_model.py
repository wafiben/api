import uuid
from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    city = models.CharField(max_length=100)
    class Meta:
        db_table = 'users'


    