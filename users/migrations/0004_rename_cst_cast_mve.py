# Generated by Django 4.1.5 on 2023-02-04 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_movies_cast'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cast',
            old_name='cst',
            new_name='mve',
        ),
    ]