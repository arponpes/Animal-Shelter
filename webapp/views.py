from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from core.models import Animal


def HomeView(request):
    animal_list = Animal.objects.exclude(state='UNAVAILABLE').order_by('-state', '?')
    paginator = Paginator(animal_list, 9)
    page = request.GET.get('page')
    animals = paginator.get_page(page)
    return render(request, 'webapp/home.html', {'animals': animals})


class FrequentQuestionsView(TemplateView):
    template_name = 'webapp/frequent_questions.html'


class AboutUsView(TemplateView):
    template_name = 'webapp/about_us.html'


class HelpView(TemplateView):
    template_name = 'webapp/help.html'


class ContactView(TemplateView):
    template_name = 'webapp/contact.html'


class AnimalDetail(DetailView):
    model = Animal
    template_name = 'webapp/animal_detail.html'
