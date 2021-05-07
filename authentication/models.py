from django.db import models
from django.utils import timezone

# Create your models here.

class Audiobook(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField()
    upload_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.name 

        
class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField()
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField()
    upload_at = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participant = models.TextField(null=True, blank= True)


    def __str__(self):
        return self.name


