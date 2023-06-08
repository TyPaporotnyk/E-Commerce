from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.formfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)   
    surname = forms.CharField(max_length=100) 
    phone_number = PhoneNumberField()
    email = forms.EmailField()

    city = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    house_number = forms.CharField(max_length=100)
    post_office = forms.CharField(max_length=100)
