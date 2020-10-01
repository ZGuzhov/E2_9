from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
import threading


class EmailList(models.Model):
    message = models.CharField(max_length=255)
    delay = models.IntegerField()
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.message


def email_yandex(message, email=''):
    send_mail(
        'Test Email',
        message,
        'testof32@yandex.ru',
        ['zguzhov@yandex.ru', email],
        fail_silently=False
    )


@receiver(pre_save, sender=EmailList)
def send_email(sender, instance, **kwargs):
    t = threading.Timer(instance.delay, email_yandex, args=(instance.message, instance.email, ))
    t.start()
    # t.join()