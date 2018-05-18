from core.factories import AnimalFactory, AdopterFamilyFactory
import pytest


@pytest.mark.django_db
def test_unavailable_animal():
    animal = AnimalFactory(state='AVAILABLE')
    AdopterFamilyFactory(animal=animal)
    assert animal.state == 'UNAVAILABLE'

