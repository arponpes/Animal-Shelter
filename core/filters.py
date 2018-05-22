from core.models import Animal
from django_filters import FilterSet, ChoiceFilter


class AnimalFilter(FilterSet):
    animal_type = ChoiceFilter(empty_label='Todos',
                               choices=Animal.ANIMAL_TYPE_CHOICES)
    sex = ChoiceFilter(empty_label='Todos', choices=Animal.SEX_CHOICES)

    class Meta:
        model = Animal
        fields = ['animal_type', 'sex']
