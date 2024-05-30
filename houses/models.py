from django.db import models

# Create your models here.


class House(models.Model):

    '''
    Model definition for Houses
    '''
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(default=True)

    def __str__(self):  # str method 사용
        return self.name
