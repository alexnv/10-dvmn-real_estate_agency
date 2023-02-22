from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 1
    raw_id_fields = ["owner"]


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner', ]
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['who_liked', ]
    inlines = [
        OwnersInline,
    ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    fields = ("author", "flat", "text")
    raw_id_fields = ("flat", "author")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('name',)
    list_display = ('name', 'phonenumber', 'pure_phone',)
