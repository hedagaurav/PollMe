# Generated by Django 2.1a1 on 2018-06-07 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='poll',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]
