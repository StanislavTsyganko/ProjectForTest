from django import forms
from . import models

class CreateCitate(forms.ModelForm):
    class Meta:
        model = models.Citata
        fields = ['content', 'character', 'weight']
        labels = {"content":"Цитата", "character": "Персонаж или автор", "weight":"Вес"}