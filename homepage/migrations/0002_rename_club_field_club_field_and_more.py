# Generated by Django 4.1.3 on 2022-11-30 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='club_field',
            new_name='field',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='club_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='club_type',
            new_name='type',
        ),
    ]
