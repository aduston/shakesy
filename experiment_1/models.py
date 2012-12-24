from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    #cimage = models.ImageField(upload_to="character_images")
    description = models.TextField(max_length=8191)

class Scene(models.Model):
    act = models.IntegerField()
