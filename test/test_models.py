import pytest

from core.factories import AdopterFamilyFactory, AnimalFactory


@pytest.mark.django_db
def test_unavailable_animal():
    animal = AnimalFactory(state='AVAILABLE')
    AdopterFamilyFactory(animal=animal)
    assert animal.state == 'UNAVAILABLE'
