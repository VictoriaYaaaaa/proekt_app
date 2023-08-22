from django import forms
from django.db import models
from .models import Advertisement

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields=('title','description','price','auction','image')
        widgets= {
            'title':forms.TextInput(attrs={'rows':'10', 'class':'form-control form-control-lg'}),
            'description':forms.Textarea(attrs={'class':'form-control form-control-lg'}),
            'price':forms.NumberInput(attrs={'class':'form-control form-control-lg'}),
            'auction':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'image':forms.FileInput(attrs={'class':'form-control form-control-lg'})
            }
    def clean_title(self):
        data=self.cleaned_data['title']
        if data[0]=='?':
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака, передалайте!")
        return data
        



