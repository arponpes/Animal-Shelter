from django.contrib import admin
from .models import Animal, Person, AdopterFamily, Foster


class AnimalAdmin(admin.ModelAdmin):
    list_diplay = ('name',
                   'birth_date',
                   'entry_date', 'departure_date', 'sex', 'animal_type', 'state',)


class PersonAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'last_name', 'email', 'address', 'phone')


class AdopterFamilyAdmin(admin.ModelAdmin):
    list_display = ('animal', 'person')


class FosterAdmin(admin.ModelAdmin):
    list_display = ('animal', 'person')


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(AdopterFamily, AdopterFamilyAdmin)
admin.site.register(Foster, FosterAdmin)
