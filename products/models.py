from django.db import models

# Create your models here.

class Candle(models.Model):
    """
    Represents a candle product with name, price, image, and description.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='candles/')
    description = models.TextField()

    def __str__(self):
        """
        Returns the name of the candle for display purposes.
        """
        return self.name


class RoomSpray(models.Model):
    """
    Represents a room spray product with name, price, image, and description.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='room_sprays/')
    description = models.TextField()

    def __str__(self):
        """
        Returns the name of the room spray for display purposes.
        """
        return self.name
