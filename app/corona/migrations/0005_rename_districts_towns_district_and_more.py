# Generated by Django 5.0.7 on 2024-08-13 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0004_towns'),
    ]

    operations = [
        migrations.RenameField(
            model_name='towns',
            old_name='districts',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='towns',
            old_name='states',
            new_name='state',
        ),
    ]
