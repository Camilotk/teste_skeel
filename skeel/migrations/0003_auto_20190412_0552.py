# Generated by Django 2.2 on 2019-04-12 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeel', '0002_auto_20190412_0549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benefits',
            old_name='vaga',
            new_name='job_vacancy',
        ),
    ]
