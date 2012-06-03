#coding=utf-8
from django import forms
from django.contrib.auth import models as auth_models


def _username_registered(self):
    '''check if the username is registered already'''
    users = auth_models.User.objects.filter(
            username__iexact=self.cleaned_data["username"])
    if users:
        return True
    return False
        
def _username_valid(self):
    if '@' in self.cleaned_data["username"]:
        return False
    return True


def _email_registered(self):
    '''check if the email has been registered already, django will check correctness；'''
    emails = auth_models.User.objects.filter(
            email__iexact=self.cleaned_data["email"])
    if emails:
        return True
    return False

class RegisterForm(forms.Form):
    '''form for user registeration'''
    email = forms.EmailField(label="Email", max_length=30, widget=forms.TextInput(attrs={'size': 20,'class':'class_email',}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'size': 20,'class':'class_password',}))
    username = forms.CharField(label="Nickname", max_length=30, widget=forms.TextInput(attrs={'size': 20,'class':'class_username',}))
    
    def clean_username(self):
        if _username_valid(self):
            if _username_registered(self):
                raise forms.ValidationError("this name has been registered --!")
        else:
            raise forms.ValidationError("invalid charactor '@' ")
        return self.cleaned_data["username"]

    def clean_email(self):
        if _email_registered(self):
            raise forms.ValidationError("this email has been registered ==!")
        return self.cleaned_data["email"]
        
class LoginForm(forms.Form):
    '''form for user login'''
    username=forms.CharField(label="Login or Email", max_length=30, widget=forms.TextInput(attrs={'size': 20,'class':'class_username',}),error_messages={'required': 'Please enter your name'})
    password=forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput(attrs={'size': 20,'class':'class_password',}),error_messages={'required': 'Please enter your password'})

    def clean_username(self):
        '''this can be nikename or email addr, we do not check it here'''
        return self.cleaned_data["username"]

    def clean_password(self):
        return self.cleaned_data["password"]

class UserForm(forms.Form):
    '''form to show user info'''
    username = forms.CharField(label="Nickname", max_length=30, widget=forms.TextInput(attrs={'size': 20,'class':'class_username',}))
    email = forms.EmailField(label="Email", max_length=30, widget=forms.TextInput(attrs={'size': 30,'class':'class_email',}))
    
    def clean_username(self):
        if _username_valid(self):
            if _username_registered(self):
                raise forms.ValidationError("this name has not been registered --!")
        else:
            raise forms.ValidationError("invalid charactor '@' ")
        return self.cleaned_data["username"]

    def clean_email(self):
        if _email_registered(self):
            raise forms.ValidationError("this email has been registered ==!")
        return self.cleaned_data["email"]
