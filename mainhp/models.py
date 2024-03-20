from django.db import models
from cloudinary.models import CloudinaryField

class Mainhp(models.Model):
    title = models.CharField(max_length=200)
    quote = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    image = CloudinaryField('image', default='placeholder')
    image = CloudinaryField('image', default='placeholder')
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title

    