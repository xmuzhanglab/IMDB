# Generated by Django 4.1.3 on 2023-11-17 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_sample_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='sample_id',
            new_name='sample',
        ),
    ]
