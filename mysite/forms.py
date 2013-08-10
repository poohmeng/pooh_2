__author__ = 'mengmeng'
from django import forms as forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea())
    from_email = forms.EmailField(required=False,label='Your e-mail address')
 