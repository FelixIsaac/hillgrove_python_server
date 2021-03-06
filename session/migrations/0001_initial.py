# Generated by Django 3.2.4 on 2021-07-05 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.session')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='topics',
            field=models.ManyToManyField(related_name='session_topics', to='session.Topic'),
        ),
    ]
