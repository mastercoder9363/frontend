from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    tanlov = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    rasm = models.CharField(max_length=255)

    def __str__(self):
        return self.name
