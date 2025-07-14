from django import forms
from . import models

class CreateCitate(forms.ModelForm):
    class Meta:
        model = models.Citata
        fields = ['content', 'source', 'character', 'weight']
        labels = {"content":"Цитата", "source":"Источник", "character": "Персонаж или автор", "weight":"Вес"}

# class EditCitate(forms.ModelForm):