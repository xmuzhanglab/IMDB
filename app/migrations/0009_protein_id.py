# Generated by Django 4.1.3 on 2023-10-13 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_sample_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='protein',
            name='id',
            field=models.PositiveIntegerField(db_index=True, default=0, max_length=32),
        ),
    ]
