from datetime import datetime as dt

from django.db.models import BooleanField, Case, F, When
from django.db.models.functions import Extract
from django.views.generic import DetailView, TemplateView

from django_filters.views import FilterView

from core import filters
from core.models import Animal


class HomeView(FilterView):
    model = Animal
    template_name = 'webapp/home.html'
    queryset = (Animal.objects.filter(state='URGENCY')
                .order_by('-state', 'entry_date'))
    filterset_class = filters.AnimalFilter
    context_object_name = 'animals'


class AnimalsView(FilterView):
    model = Animal
    template_name = 'webapp/animals.html'
    paginate_by = 9
    filterset_class = filters.AnimalFilter
    context_object_name = 'animals'

    def get_queryset(self):
        return (Animal.objects
                .annotate(duration=Extract(dt.now() - F('birth_date'), 'days'))
                .annotate(is_puppy=Case(When(duration__lt=365, then=True),
                          default=False, output_field=BooleanField()))
                .exclude(state='UNAVAILABLE')
                .order_by('-state', 'entry_date'))

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        aux = self.request.GET.copy()
        if aux.get('page'):
            aux.pop('page')
        data['query_get_string'] = aux.urlencode()
        return data


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

    def get_queryset(self):
        return Animal.objects.exclude(state='UNAVAILABLE')

