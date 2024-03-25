from django.db import models
from cloudinary.models import CloudinaryField

class Benefits(models.Model):
    """
    Stores a single benefit entry
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


