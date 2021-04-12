import hashlib

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'avatar', 'age', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        user = self.cleaned_data['username']
        em = ShopUser.objects.all()
        for value in em:
            if value.email == data and value.username != user:
                raise forms.ValidationError("Такой адрес электронной почты уже существует")
        return data

    def save(self):
        user = super().save()
        user.is_active = False
        user.activation_key = hashlib.sha1(user.email.encode('utf8')).hexdigest()
        user.save()

        return user



class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'avatar', 'age', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        user = self.cleaned_data['username']
        em = ShopUser.objects.all()
        for value in em:
            if value.email == data and value.username != user:
                raise forms.ValidationError("Такой адрес электронной почты уже существует")
        return data
