from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from accounts.models import User


class AuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    # profile_photo = forms.ImageField(
    #     label='Фото профиля',
    #     widget=forms.FileInput(attrs={'class': 'form-control'}),
    #     required=False
    # )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'profile_photo']
