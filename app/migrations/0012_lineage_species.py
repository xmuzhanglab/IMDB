# Generated by Django 4.1.3 on 2023-11-13 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_protein_position_protein'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineage',
            name='species',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.species'),
        ),
    ]
