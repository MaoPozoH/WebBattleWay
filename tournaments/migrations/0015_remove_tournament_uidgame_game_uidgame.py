# Generated by Django 5.0.2 on 2024-03-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0014_alter_tournament_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='UIDGame',
        ),
        migrations.AddField(
            model_name='game',
            name='UIDGame',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='UID'),
        ),
    ]
