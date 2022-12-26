from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=125)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('home_detail', args=[str(self.id)])

