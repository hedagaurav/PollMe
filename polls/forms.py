from django import forms
from .models import Poll, Choice


class PollForm(forms.ModelForm):
    choice1 = forms.CharField(label='First Choice', max_length=100, min_length=5,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    choice2 = forms.CharField(label='Second Choice', max_length=100, min_length=2,
                              widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Poll
        fields = ['text', 'choice1', 'choice2']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'cols': 10, 'rows': 5})
        }


class EditPollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'cols': 10, 'rows': 5})
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
