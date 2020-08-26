from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import re

def validate_name(name):
    m=re.match('[a-zA-Z]+',name)
    if m.group()!=name:
        raise ValidationError('name is not valid')
    return name

class SampleForm(forms.Form):
    name=forms.CharField(max_length=200,required=True,label="name :",
    validators=[validate_name])

    last_name=forms.CharField(max_length=200,required=True,label="last name :")

    email=forms.EmailField(max_length=200,required=True,label="email :",
    validators=[validators.MinLengthValidator(10)])

    confirm_email=forms.EmailField(max_length=100,required=True,label="confirm email :",)
    
    pwd=forms.CharField(max_length=100,required=True,label="password :",widget=forms.PasswordInput(attrs={'placeholder':"password"}))

    pic=forms.ImageField(max_length=200,required=True,label="pic :")

    def clean(self,*args,**kwargs):
        cleaned_data=super().clean()#getting all the data that is filled in the form
        email=cleaned_data.get("email")
        cemail=cleaned_data.get("confirm_email")
        if email==cemail:
            return cleaned_data
        self.add_error('confirm_email',"Both the emails are not same")#this method will decide to which field we need to show the error
        #self.add_error("fieldname",error message)

