from turtle import title
from django.db import models

# Create your models here

class book(models.Model):
    title = models.CharField(max_length=200)
    number_of_pages = models.IntegerField()
    published_date = models.DateField()
    quantity = models.IntegerField()

    # used to return name for an object
    def __str__(self):
        return self.title 


