# Generated by Django 5.0.2 on 2024-02-21 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0007_remove_tournament_game_alter_user_points'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'game', 'verbose_name_plural': 'games'},
        ),
        migrations.AddField(
            model_name='tournament',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.game', verbose_name='Juego'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='status',
            field=models.CharField(choices=[('C', 'Creado'), ('O', 'En curso'), ('E', 'Finalizado')], default='C', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterModelTable(
            name='game',
            table='games',
        ),
    ]
