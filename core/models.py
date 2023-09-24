from django.db import models

class Car(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    description = models.TextField()