from django_filters import ChoiceFilter, FilterSet

from core.models import Animal

AGE_CHOICES = (
    ('False', 'Adultos'),
    ('True', 'Cachorros')
)


class AnimalFilter(FilterSet):
    animal_type = ChoiceFilter(empty_label='Todos',
                               choices=Animal.ANIMAL_TYPE_CHOICES)
    sex = ChoiceFilter(empty_label='Todos', choices=Animal.SEX_CHOICES)
    size = ChoiceFilter(empty_label='Todos', choices=Animal.SIZE_CHOICES)
    is_puppy = ChoiceFilter(empty_label='Todos', choices=AGE_CHOICES)

    class Meta:
        model = Animal
        fields = ['animal_type', 'sex', 'size', 'is_puppy']
