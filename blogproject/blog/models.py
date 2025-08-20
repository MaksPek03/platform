from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length = 20, unique=True)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    def __str__(self):
        return self.title
    
    
class Uwaga(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    severity = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True, null=True, blank=True )