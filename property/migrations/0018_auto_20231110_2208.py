# Generated by Django 2.2.24 on 2023-11-10 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_remove_owner_owners_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='phonenumber',
        ),
    ]
