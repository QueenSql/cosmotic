from django.db import models

# Create your models here.

class Candle(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='candles/')
    description = models.TextField()

    def __str__(self):
        return self.name

class RoomSpray(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='room_sprays/')
    description = models.TextField()

    def __str__(self):
        return self.name
