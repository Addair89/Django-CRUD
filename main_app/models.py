from django.db import models
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year_released = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})