from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'homeapp/home.html'

class AboutPageView(TemplateView):
    template_name = 'homeapp/about.html'

class ContactPageView(FormView):
    form_class = ContactForm
    template_name = 'homeapp/contact.html'

    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        print(form.cleaned_data)
        return super().form_valid(form)


