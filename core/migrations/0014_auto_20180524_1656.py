# Generated by Django 2.0.5 on 2018-05-24 14:56

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180524_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='uploaded', verbose_name='Imagen'),
        ),
    ]