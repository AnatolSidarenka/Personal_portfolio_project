from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now=True)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title