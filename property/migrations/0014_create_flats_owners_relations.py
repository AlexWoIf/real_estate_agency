# Generated by Django 2.2.24 on 2023-11-10 07:08

from django.db import migrations


def flats_owners_relations(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator(chunk_size=1000):
        owner = Owner.objects.filter(
            owners_phonenumber=flat.owners_phonenumber
        ).first()
        if owner:
            flat.owned_by.add(owner)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20231110_0959'),
    ]

    operations = [
        migrations.RunPython(flats_owners_relations)
    ]
