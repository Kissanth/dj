from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=52)

   #
  #  description = models.CharField(max_length=79)
    
