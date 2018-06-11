from rest_framework import viewsets

from api import serializers

from core import models


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = models.Animal.objects.all()
    serializer_class = serializers.AnimalSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class FosterViewSet(viewsets.ModelViewSet):
    queryset = models.Foster.objects.all()
    serializer_class = serializers.FosterSerializer


class AdopterFamilyViewSet(viewsets.ModelViewSet):
    queryset = models.AdopterFamily.objects.all()
    serializer_class = serializers.AdopterFamilySerializer
