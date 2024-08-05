from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'id_email',
        'required': 'required'
    }))
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'id_username',
        'required': 'required'
    }))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'id_password1',
        'required': 'required'
    }))
    password2 = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'id_password2',
        'required': 'required'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
