from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    # use widget to edit the attributes of form fields.
    username = forms.CharField(label='Username', max_length=50, min_length=5, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    # or we can use widgets like
    # username.widget.attrs.update({'class': 'form-control'})
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', max_length=50, min_length=5, required=True,
                                widget=forms.PasswordInput)
    password1.widget.attrs.update({'class': 'form-control'})
    password2 = forms.CharField(label='Confirm Password', max_length=50, min_length=5, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Email already registered.')
        return email

    # def clean_password1(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('p1 does not match p2')
    #     return p1
    # clean_password1 will raise a key error
    # because it references password2 which is ran after password1 validation.

    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('p2 does not match p1')
    #     return p2
    # clean_password2 will run and check for the 2 passwords are same or not.

    def clean(self):
        cleaned_data = super().clean()
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('Passwords Do not match.')
        # here it raises a non field error
        # check its documentation
