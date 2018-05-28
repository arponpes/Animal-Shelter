from core import factories
from core import services


def test_generate_unique_file_path():
    instance = factories.AnimalFactory.build()
    file_path = services.generate_unique_file_path(instance, 'uploaded.jpeg')
    assert file_path.endswith('.jpeg')
