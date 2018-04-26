from django.db import models

# Create your models here.

class Page(models.Model):
    url = models.CharField(max_length=64)
    content = models.TextField()
    def __str__(self):
        return self.url
