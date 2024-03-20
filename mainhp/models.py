from django.db import models
from cloudinary.models import CloudinaryField

class Mainhp(models.Model):
    title = models.CharField(max_length=200)
    quote = models.CharField(max_length=150)
    content = models.TextField()
 
    