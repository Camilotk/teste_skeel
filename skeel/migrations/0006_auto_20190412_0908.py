# Generated by Django 2.2 on 2019-04-12 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skeel', '0005_auto_20190412_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobbenefit',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefit_job', to='skeel.JobVacancy'),
        ),
    ]
