from django.db import models
from django.utils import timezone

class AppVariety(models.Model):
    APP_TYPE_CHOICE = [
        ('ag', 'agriculture'),
        ('so', 'social'),
        ('ec', 'eco'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)


def __str__(self):
    return self.name
