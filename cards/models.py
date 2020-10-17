from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Card(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])
        
