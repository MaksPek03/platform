from django.db import models

# Create your models here.
class member(models.Model):
    fistname = models.CharField(max_length = 40)