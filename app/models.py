from django.db import models

# Create your models here.

class Jsp(models.Model):
    trainer=models.CharField(max_length=100)
    cleaner=models.CharField(max_length=100)
    NO_OF_staff=models.IntegerField()