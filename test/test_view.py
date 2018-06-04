import pytest

from core import factories, forms


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


@pytest.mark.django_db
def test_sitemap(client):
    response = client.get('/sitemap.xml')
    animal1 = factories.AnimalFactory(name='test1', state='UNAVAILABLE')
    animal2 = factories.AnimalFactory(name='test', state='AVAILABLE')

    assert 200 == response.status_code
    assert '/contacto' in response.rendered_content
    assert animal1.slug not in response.rendered_content
    assert animal2.slug in response.rendered_content


def test_contact_form():
    form_data = {'subject': 'Duda',
                 'email': 'duda@gmail.com',
                 'name': 'Juan',
                 'message': 'Estoy comprobando que el formato'}

    form = forms.ContactForm(data=form_data)

    assert form.is_valid(), form.errors
