# Generated by Django 2.2.24 on 2023-02-20 07:32

from django.db import migrations
from django.db.models import F


def fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(new_building=F('construction_year') >= 2015)

def backward_fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(new_building=None)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building, backward_fill_new_building)
    ]


