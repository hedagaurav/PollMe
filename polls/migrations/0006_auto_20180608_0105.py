# Generated by Django 2.1a1 on 2018-06-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_choice_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='poll',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='poll',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
