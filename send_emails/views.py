from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView
from send_emails.forms import ContactForm
from send_emails.models import EmailList
from django.urls import reverse_lazy


class OkView(TemplateView):

     template_name = 'ok.html'


class MainView(CreateView):
    model = EmailList
    form_class = ContactForm  
    success_url = reverse_lazy('ok')
    template_name = 'main.html'  


class EmailListView(ListView):

    model = EmailList

    def get_queryset(self):
        n = EmailList.objects.all().count()
        context = EmailList.objects.all()[n-10:n]
        return context
