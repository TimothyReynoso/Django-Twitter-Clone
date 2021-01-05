from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField()
    displayname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()