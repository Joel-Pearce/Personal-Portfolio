from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    post = models.TextField()

    def __str__(self):
        return self.title


