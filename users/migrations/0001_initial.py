# Generated by Django 3.2.4 on 2021-07-05 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '0001_initial'),
        ('authentication', '0008_alter_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.session')),
                ('last_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]
