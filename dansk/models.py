from django.db import models

# Create your models here.
class Alfabet(models.Model):
    image = models.ImageField(upload_to='images/')
    danord = models.CharField(max_length=50, blank = True)
    tysord = models.CharField(max_length=50, blank = True)
    engord = models.CharField(max_length=50, blank = True)
    danbe = models.TextField(blank=True)
    tysbe = models.TextField(blank=True)
    engbe = models.TextField(blank=True)
    bogstav = models.ManyToManyField('bogstav', related_name='item')


    def __str__(self):
        return self.danord
    
class Bogstav(models.Model):
    bogstav = models.CharField(max_length=10)

    def __str__(self):
        return self.bogstav