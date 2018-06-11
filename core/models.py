import os

from django.conf import settings
from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnDiscPlaceholderImage

from core.services import generate_unique_file_path

NO_IMAGE_PLACEHOLDER = OnDiscPlaceholderImage(
    path=os.path.join(settings.PROJECT_DIR,
                      'static',
                      'img',
                      'no-image-placeholder.png'),
)


class TimeStampleModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class Animal(TimeStampleModel):
    ANIMAL_TYPE_CHOICES = (
        ('DOG', 'Perro'),
        ('CAT', 'Gato'),
    )
    SEX_CHOICES = (
        ('MALE', 'Macho'),
        ('FEMALE', 'Hembra'),
    )
    STATE_CHOICES = (
        ('AVAILABLE', 'Disponible'),
        ('UNAVAILABLE', 'No Disponible'),
        ('URGENCY', 'Urgente')
    )
    SIZE_CHOICES = (
        ('BIG', 'Grande'),
        ('MEDIUM', 'Mediano'),
        ('LITTLE', 'Pequeño'),
    )
    name = models.CharField('Nombre', max_length=50)
    birth_date = models.DateField('Fecha de nacimiento')
    entry_date = models.DateField('Fecha de entrada')
    departure_date = models.DateField(
        'Fecha de salida',
        blank=True,
        null=True
        )
    description = models.TextField(
        'Descripcion',
        blank=True,
        null=True
        )
    image = VersatileImageField(
        'Imagen',
        null=True,
        blank=True,
        upload_to=generate_unique_file_path,
        placeholder_image=NO_IMAGE_PLACEHOLDER
        )
    size = models.CharField(
        'Tamaño',
        max_length=50,
        choices=SIZE_CHOICES, default='MEDIUM'
        )
    animal_type = models.CharField(
        'Tipo',
        max_length=50,
        choices=ANIMAL_TYPE_CHOICES,
        default='DOG'
        )
    sex = models.CharField(
        'Sexo',
        max_length=50,
        choices=SEX_CHOICES,
        default='MALE'
        )
    state = models.CharField(
        'Estado',
        max_length=50,
        choices=STATE_CHOICES,
        default='UNAVAILABLE'
        )
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return f'{self.name} {self.animal_type}'

    def get_absolute_url(self):
        return reverse('animal_detail', args=[self.slug])


class Person(TimeStampleModel):
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=70)
    phone = models.CharField('Telefono', max_length=20)
    address = models.CharField('Direccion', max_length=100)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Foster(TimeStampleModel):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)


class AdopterFamily(TimeStampleModel):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.animal.state = 'UNAVAILABLE'
        self.animal.save()
