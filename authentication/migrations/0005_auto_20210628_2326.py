# Generated by Django 3.2.4 on 2021-06-28 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_delete_session'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='familyName',
            new_name='family_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='googleId',
            new_name='google_id',
        ),
    ]
