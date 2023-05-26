# Generated by Django 3.2.18 on 2023-05-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_person', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Persona')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellido')),
                ('nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(blank=True, max_length=30, verbose_name='Género')),
                ('nacionalidad', models.CharField(blank=True, max_length=55, verbose_name='Nacionalidad')),
                ('email', models.EmailField(max_length=255, verbose_name='Correo electrónico')),
                ('celular_1', models.IntegerField(verbose_name='Celular')),
                ('rol', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_person', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Persona')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellido')),
                ('nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(blank=True, max_length=30, verbose_name='Género')),
                ('nacionalidad', models.CharField(blank=True, max_length=55, verbose_name='Nacionalidad')),
                ('email', models.EmailField(max_length=255, verbose_name='Correo electrónico')),
                ('celular_1', models.IntegerField(verbose_name='Celular')),
                ('cuil', models.CharField(max_length=10, unique=True, verbose_name='CUIL')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
    ]
