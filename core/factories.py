import factory
from core import models
from .models import Animal
import factory.fuzzy

animal_state = [state[0] for state in models.Animal.STATE_CHOICES]
animal_sex = [sex[0] for sex in models.Animal.SEX_CHOICES]
animal_type = [type[0] for type in models.Animal.ANIMAL_TYPE_CHOICES]


class AnimalFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Animal

    name = factory.Faker('last_name')
    birth_date = factory.Faker('date')
    entry_date = factory.Faker('date')
    animal_type = factory.fuzzy.FuzzyChoice(choices=animal_type)
    sex = factory.fuzzy.FuzzyChoice(choices=animal_sex)
    state = factory.fuzzy.FuzzyChoice(choices=animal_state)
    description = factory.Faker('text')
    

    