# Generated by Django 5.0.7 on 2024-07-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
