from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Animal
from django.views.generic.list import ListView


class HomeView(ListView):
    model = Animal
    template_name = 'webapp/home.html'


class FrequentQuestionsView(TemplateView):
    template_name = 'webapp/frequent_questions.html'


class AboutUsView(TemplateView):
    template_name = 'webapp/about_us.html'


class HelpView(TemplateView):
    template_name = 'webapp/help.html'


class ContactView(TemplateView):
    template_name = 'webapp/contact.html'
