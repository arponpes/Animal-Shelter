from django.db import models


class Pet(models.Model):
    name = models.CharField('Nombre', max_length=50)
    birth_date = models.DateField('Fecha de nacimiento')
    entry_date = models.DateField('Fecha de entrada')
    departure_date = models.DateField('Fecha de salida', blank=True, null=True)
    PET_TYPE_CHOICES = (
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
    )
    pet_type = models.CharField('Tipo',
                                max_length=10,
                                choices=PET_TYPE_CHOICES, default='DOG')
    SEX_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    sex = models.CharField('Sexo',
                           max_length=10, choices=SEX_CHOICES, default='MALE')
    STATE_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('UNAVAILABLE', 'Unavailable'),
        ('URGENCY', 'Urgency')
    )
    state = models.CharField('Estado',
                             max_length=10,
                             choices=STATE_CHOICES, default='Unavailable')


class Person(models.Model):
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=70)
    phone = models.CharField('Telefono', max_length=12)
    address = models.CharField('Direccion', max_length=100)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)


class Foster(models.Model):
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE,)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)


class AdopterFamily(models.Model):
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE,)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    