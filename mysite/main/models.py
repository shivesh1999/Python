from django.db import models

# Create your models here.

# inherting django model
class tutorial(models.Model):
    tutorial_title = models.CharField(max_length=30)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published")

    # used to return name for an object
    def __str__(self):
        return self.tutorial_title 
