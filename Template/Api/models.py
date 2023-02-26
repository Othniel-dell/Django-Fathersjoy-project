from django.db import models

# Create your models here.
class RouterOs(models.Model):
    Name = models.CharField(max_length=100)
    IP = models.TextField()
