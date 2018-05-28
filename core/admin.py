from django.contrib import admin

from .models import AdopterFamily, Animal, Foster, Person


class AnimalAdmin(admin.ModelAdmin):
    list_filter = ('animal_type', 'sex', 'state', 'size')
    list_display = ('name', 'animal_type', 'sex', 'state', 'size')
    search_fields = ('name',)


# class AnimalInline(admin.StackedInline):
#     model = Animal


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'address', 'phone', 'email')
    search_fields = ('name', 'phone')
    # inlines = [
    #     AnimalInline,
    # ]


class AdopterFamilyAdmin(admin.ModelAdmin):
    list_display = ('animal', 'person')
    list_filter = ('person__name',)


class FosterAdmin(admin.ModelAdmin):
    list_display = ('animal', 'person')
    list_filter = ('person__name',)


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(AdopterFamily, AdopterFamilyAdmin)
admin.site.register(Foster, FosterAdmin)
