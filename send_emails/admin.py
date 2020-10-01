from django.contrib import admin
from send_emails.models import EmailList


@admin.register(EmailList)
class EmailAdmin(admin.ModelAdmin):
    pass