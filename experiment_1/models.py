from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    cimage = models.ImageField(upload_to="character_images", null=True, blank=True)
    description = models.TextField(max_length=8191)

class Scene(models.Model):
    act = models.IntegerField()

class Subtitle(models.Model):
    contemporary_text = models.CharField(max_length=1024)
    original_text= models.CharField(max_length=1024)
    character = models.ForeignKey(Character, null=True, blank=True)
    start_time = models.IntegerField() # specifies time in tenths of a second
