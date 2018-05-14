from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=50)
    BIRTH_DATE = models.DateField()
    ENTRY_DATE = models.DateField()
    DAPARTURE_DATE = models.DateField(blank=True, null=True)
    TYPE_CHOICES = (
        ('DOG','Dog'),
        ('CAT', 'Cat'),
    )
    TYPE = models.CharField(max_length=10,choices=TYPE_CHOICES, default='DOG')
    SEX_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    SEX = models.CharField(max_length=10, choices=SEX_CHOICES, default='MALE')
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('UNAVAILABLE', 'Unavailable'),
        ('URGENCY', 'Urgency')
    )
    STATUS = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='Unavailable')


class Person(models.Model):
    NAME = models.CharField(max_length=50)
    LAST_NAME = models.CharField(max_length=70)
    PHONE = models.CharField(max_length=12)
    ADDRESS = models.CharField(max_length=100)
    EMAIL = models.EmailField(max_length=100, blank=True, null=True)

class Foster(models.Model):
    pet = models.ForeignKey('Pet',on_delete=models.CASCADE,)
    person = models.ForeignKey('Person',on_delete=models.CASCADE)


class AdopterFamily(models.Model):
    pet = models.ForeignKey('Pet',on_delete=models.CASCADE,)
    person = models.ForeignKey('Person',on_delete=models.CASCADE)