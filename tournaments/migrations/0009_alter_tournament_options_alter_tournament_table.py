# Generated by Django 5.0.2 on 2024-02-21 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0008_alter_game_options_tournament_game_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'verbose_name': 'tournament', 'verbose_name_plural': 'tournaments'},
        ),
        migrations.AlterModelTable(
            name='tournament',
            table='tournaments',
        ),
    ]