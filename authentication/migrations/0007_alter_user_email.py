# Generated by Django 3.2.4 on 2021-06-28 17:35

from django.db import migrations
import mirage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=mirage.fields.EncryptedEmailField(max_length=64, unique=True),
        ),
    ]
