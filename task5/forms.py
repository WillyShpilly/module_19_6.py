from platform import mac_ver

from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(max_length=8, label='Введите пароль')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль')
    age = forms.IntegerField(min_value=18, max_value=99, label="Введите возраст")
    # age = forms.CharField(max_length=3, label="Введите возраст")


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Ваше имя')
#     email = forms.EmailField(label='Email')
#     message = forms.CharField(widget=forms.Textarea, label='Сообщение')
#     subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку')