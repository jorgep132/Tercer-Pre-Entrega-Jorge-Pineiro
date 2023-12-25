# Generated by Django 5.0 on 2023-12-25 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrega3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estudiante', models.CharField(max_length=20)),
                ('apellido_estudiante', models.CharField(max_length=20)),
                ('email_estudiante', models.EmailField(max_length=254)),
                ('DNI_estudiante', models.IntegerField(validators=[django.core.validators.MinValueValidator(8, message='El DNI debe tener al menos 7 dígitos.'), django.core.validators.MaxValueValidator(9, message='El DNI no puede tener más de 8 dígitos.')])),
            ],
        ),
    ]
