from django.db import models
from django.urls import reverse
REASONS = (
    ('O', 'Game was to old'),
    ('H', 'Game was to hard'),
    ('E', 'Game was to easy')
)

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stores_detail', kwargs={'pk': self.id})

class Game(models.Model):
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year_released = models.IntegerField()
    store = models.ManyToManyField(Store)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    
class Owner(models.Model):
    name = models.CharField(max_length=100)
    last_played = models.DateField('Played Game Last On Date')
    reason_thrown_away = models.CharField(max_length=1, choices=REASONS, default=REASONS[0][0])
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_reason_thrown_away_display()} on {self.date}'
    
    class Meta:
        ordering = ['-name']