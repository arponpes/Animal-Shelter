# Generated by Django 2.0.5 on 2018-05-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180516_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_type',
            field=models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat')], default='DOG', max_length=50, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=50, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='state',
            field=models.CharField(choices=[('AVAILABLE', 'Available'), ('UNAVAILABLE', 'Unavailable'), ('URGENCY', 'Urgency')], default='UNAVAILABLE', max_length=50, verbose_name='Estado'),
        ),
    ]
