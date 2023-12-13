from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_lenght=50)
    password = forms.CharField(widget=forms.PasswordInput)