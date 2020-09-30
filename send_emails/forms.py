from django import forms
from django.core.mail import send_mail
import threading
from send_emails.models import threads


def email_yandex(message, email=''):
    send_mail(
        'Test Email',
        message,
        'testof32@yandex.ru',
        ['zguzhov@yandex.ru', email],
        fail_silently=False
    )


class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    delay = forms.IntegerField(widget=forms.NumberInput)
    email = forms.EmailField(max_length=256, required=False)

    def send_email(self):
        t = threading.Timer(self.cleaned_data['delay'], email_yandex, args=(self.cleaned_data['message'], self.cleaned_data['email'], ))
        threads.append('Письмо с текстом: ' + self.cleaned_data['message'] + ', с задержкой: ' + str(self.cleaned_data['delay']) + ' сек')
        t.start()
        # t.join()