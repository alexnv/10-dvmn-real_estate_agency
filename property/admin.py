from django.contrib import admin

from .models import Flat, Complaint, Owner

class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 1
    raw_id_fields=["owner"]

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner',]
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['users_who_liked',]
    inlines = [
        OwnersInline,
    ]

class ComplaintAdmin(admin.ModelAdmin):
    fields = ("author", "flat", "text")
    raw_id_fields = ("flat", "author")

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('name',)
    list_display = ('name', 'owners_phonenumber', 'owner_pure_phone',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
