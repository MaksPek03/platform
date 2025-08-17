from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
class Uwaga(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    severity = models.IntegerField()