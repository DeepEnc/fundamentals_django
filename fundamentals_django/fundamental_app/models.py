from django.db import models
from django.utils import timezone

class AppVariety(models.Model):
    APP_TYPE_CHOICE = [
        ('social', 'agriculture'),
        ('tech', 'social'),
        ('life', 'eco'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fundamental_app/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=6, choices=APP_TYPE_CHOICE)
