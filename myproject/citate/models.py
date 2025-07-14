from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Citata(models.Model):
    content = models.TextField(unique=True)
    character = models.CharField(max_length=75)
    source = models.CharField(max_length=75, default='Не известно')
    date = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default=1)
    views = models.IntegerField(default=0)
    raiting = models.IntegerField(default=0)
    user_name = models.CharField(max_length=75, default='Анонимно')

    def __str__(self):
        return self.content