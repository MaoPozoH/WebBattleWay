# Generated by Django 5.0.2 on 2024-03-10 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0011_tournament_uidgame_alter_tournament_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='UIDGame',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='UID'),
        ),
    ]
