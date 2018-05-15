from django.contrib import admin
from .models import Pet, Person, AdopterFamily, Foster


class PetAdmin(admin.ModelAdmin):
    list_diplay = ('NAME',
                   'BIRTH_DATE',
                   'ENTRY_DATE', 'DAPARTURE_DATE', 'SEX', 'TYPE', 'STATUS',)


class PersonAdmin(admin.ModelAdmin):
    list_diplay = ('NAME', 'LAST_NAME', 'EMAIL', 'ADDRESS', 'PHONE')


class AdopterFamilyAdmin(admin.ModelAdmin):
    list_display = ('pet', 'person')


class FosterAdmin(admin.ModelAdmin):
    list_display = ('pet', 'person')


admin.site.register(Pet, PetAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(AdopterFamily, AdopterFamilyAdmin)
admin.site.register(Foster, FosterAdmin)
