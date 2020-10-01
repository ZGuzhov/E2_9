from django import forms
from django.core.mail import send_mail
import threading
from send_emails.models import EmailList


class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)
    delay = forms.IntegerField(widget=forms.NumberInput)
    email = forms.EmailField(max_length=256, required=False)

    class Meta:  
        model = EmailList
        fields = '__all__'