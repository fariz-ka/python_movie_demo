from django.db import models
from django import forms


# Create your models here.
class Movie(models.Model):
    Name = models.CharField(max_length=250)
    Dis = models.TextField()
    Year = models.IntegerField()
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.Name


