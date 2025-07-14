from django import forms
from . import models
from django.core.exceptions import ValidationError

class CreateCitate(forms.ModelForm):
    class Meta:
        model = models.Citata
        fields = ['content', 'source', 'character', 'weight', 'user_name']
        labels = {
            "content": "Цитата",
            "source": "Источник", 
            "character": "Персонаж или автор",
            "weight": "Вес"
        }
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        
        if self.request and self.request.COOKIES.get('quote_user'):
            self.fields['user_name'].widget = forms.HiddenInput()
            self.fields['user_name'].initial = self.request.COOKIES['quote_user']
        else:
            self.fields['user_name'].widget = forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оставьте пустым для анонимной публикации'
            })
            self.fields['user_name'].label = "Ваше имя"
            self.fields['user_name'].required = False

    def clean(self):
        cleaned_data = super().clean()
        
        if (self.request and self.request.COOKIES.get('quote_user') 
            and isinstance(self.fields['user_name'].widget, forms.HiddenInput)):
            cleaned_data['user_name'] = self.fields['user_name'].initial
        
        user_name = cleaned_data.get('user_name', '').strip()
        if not user_name:
            cleaned_data['user_name'] = 'Анонимно'
        
        source = cleaned_data.get('source')
        if source:
            count = models.Citata.objects.filter(source=source).count()
            if count >= 3:
                raise ValidationError(
                    f'Нельзя добавить более 3 цитат из одного источника. Уже есть {count} цитат из "{source}".')
        
        return cleaned_data