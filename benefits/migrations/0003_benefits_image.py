# Generated by Django 4.2.11 on 2024-03-20 13:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0002_benefits_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefits',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]