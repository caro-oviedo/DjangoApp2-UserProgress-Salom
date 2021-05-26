from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse 
from embed_video.fields import EmbedVideoField

    

class Level(models.Model):
    number = models.CharField(max_length=5)

    def __str__(self):
        return self.number

class Trick(models.Model):
    name = models.CharField(max_length=250)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    video1 = EmbedVideoField() 
    video2 = EmbedVideoField() 
    video3 = EmbedVideoField()
    link_video1 = models.CharField(max_length=250, default=1)
    link_video2 = models.CharField(max_length=250, default=2)
    link_video3 = models.CharField(max_length=250, default=3)
    def __str__(self):
        return self.name

class Done(models.Model):
    trick = models.ForeignKey(Trick, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    date_completed = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.trick.name
    
    def get_absolute_url(self):
        return reverse('slalom:trick-detail', kwargs={'pk': self.pk})

    
# Create your models here.
