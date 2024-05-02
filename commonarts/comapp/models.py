from django.db import models

# Create your models here.
from django.conf import settings


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.title

