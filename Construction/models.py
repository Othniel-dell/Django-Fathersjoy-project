from django.db import models

# Create your models here.

class Land(models.Model):
    Name = models.CharField(max_length=200)