# Generated by Django 2.2.24 on 2023-02-22 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230221_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='users_who_liked',
            new_name='who_liked',
        ),
    ]