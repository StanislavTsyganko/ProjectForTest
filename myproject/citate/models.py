from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Citata(models.Model):
    content = models.TextField(unique=True)
    character = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default=0)
    views = models.IntegerField(default=0)
    raiting = models.IntegerField(default=0)

    def __str__(self):
        return self.content