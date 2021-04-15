from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title
