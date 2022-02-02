from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'comment', 'rating']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
            }),
            'comment': Textarea(attrs={
                'class': "form-control", 
                'style': "height:500px;"
            }),
            'rating': Select(attrs={
                'class': "form-control text-center",
            })
        }
