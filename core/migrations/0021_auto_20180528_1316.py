# Generated by Django 2.0.5 on 2018-05-28 11:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_animal_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]