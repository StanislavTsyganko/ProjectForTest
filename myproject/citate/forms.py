from django import forms
from . import models
from django.core.exceptions import ValidationError

class CreateCitate(forms.ModelForm):
    class Meta:
        model = models.Citata
        fields = ['content', 'source', 'character', 'weight']
        labels = {"content":"Цитата", "source":"Источник", "character": "Персонаж или автор", "weight":"Вес"}
    
    def clean():
        cleaned_data = super().clean()
        source = cleaned_data.get('source')

        if source:
            count = models.Citata.objects.filter(source=source).count()
            if count>=3:
                raise ValidationError(
                    f'Нельзя добавить более 3 цитат из одного источника. Уже есть {count} цитат из "{source}".')
        return cleaned_data
