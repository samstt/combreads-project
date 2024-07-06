from django.db import models

# Create your models here.

class DailyReco(models.Model):
    name = models.TextField()
    location = models.TextField()
    date = models.DateField(unique=True)

    def __str__(self):
        return f'Text for {self.date}'