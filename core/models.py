from django.db import models


class Animal(models.Model):
    ANIMAL_TYPE_CHOICES = (
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
    )
    SEX_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    STATE_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('UNAVAILABLE', 'Unavailable'),
        ('URGENCY', 'Urgency')
    )
    name = models.CharField('Nombre', max_length=50)
    birth_date = models.DateField('Fecha de nacimiento')
    entry_date = models.DateField('Fecha de entrada')
    departure_date = models.DateField('Fecha de salida', blank=True, null=True)
    animal_type = models.CharField('Tipo',
                                   max_length=10,
                                   choices=ANIMAL_TYPE_CHOICES, default='DOG')
    sex = models.CharField('Sexo',
                           max_length=10, choices=SEX_CHOICES, default='MALE')
    state = models.CharField('Estado',
                             max_length=10,
                             choices=STATE_CHOICES, default='Unavailable')

    def __str__(self):
        return f'{self.name} {self.animal_type}'


class Person(models.Model):
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=70)
    phone = models.CharField('Telefono', max_length=12)
    address = models.CharField('Direccion', max_length=100)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Foster(models.Model):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)


class AdopterFamily(models.Model):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    