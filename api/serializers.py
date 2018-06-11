from rest_framework import serializers

from core import models


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animal
        fields = (
            'name',
            'birth_date',
            'entry_date',
            'departure_date',
            'description',
            'image',
            'size',
            'animal_type',
            'sex',
            'state',
            'slug',
            )


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = (
            'name',
            'last_name',
            'phone',
            'address',
            'email'
        )


class FosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Foster
        fields = (
            'animal',
            'person',
        )


class AdopterFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdopterFamily
        fields = (
            'animal',
            'person',
        )
