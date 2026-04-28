from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        label='Profile Picture',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['image']