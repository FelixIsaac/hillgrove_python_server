# Generated by Django 3.2.4 on 2021-06-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.CharField(default=None, max_length=3),
        ),
    ]
