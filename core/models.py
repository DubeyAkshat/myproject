from django.db import models

class Car(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField()
    description = models.TextField()