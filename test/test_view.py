import pytest

from core import factories


@pytest.mark.django_db
def test_home(client):
    factories.AnimalFactory(name='test', state='URGENCY')
    response = client.get('/')
    assert 200 == response.status_code
    assert 'test' in response.rendered_content


@pytest.mark.django_db
def test_detail(client):
    animal = factories.AnimalFactory(name='test', state='AVAILABLE')
    response = client.get(animal.get_absolute_url())
    assert 200 == response.status_code
    assert 'test' in response.rendered_content


@pytest.mark.django_db
def test_animal_detail_view_404_with_invalid_status(client):
    animal = factories.AnimalFactory(state='UNAVAILABLE')
    response = client.get(animal.get_absolute_url())
    assert 404 == response.status_code
