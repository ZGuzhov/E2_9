from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from send_emails.forms import ContactForm
from send_emails.models import threads


class OkView(TemplateView):

     template_name = 'ok.html'


class MainView(FormView):
    template_name = 'main.html'
    form_class = ContactForm
    success_url = '/ok/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


def ListEmail(request):
    threads_10 = threads[:10]
    context = {"list": threads_10}
    return render(request, "list.html", context=context)