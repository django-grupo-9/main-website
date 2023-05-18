# Generated by Django 3.2.18 on 2023-05-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(max_length=30, verbose_name='Sede')),
                ('direccion', models.CharField(max_length=35, verbose_name='Dirección')),
                ('referente', models.CharField(max_length=15, verbose_name='Referente')),
                ('celular', models.CharField(max_length=10, verbose_name='Celular')),
            ],
            options={
                'verbose_name': 'Sede',
                'verbose_name_plural': 'Sedes',
            },
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id_comision', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='ID Comisión')),
                ('comision', models.CharField(max_length=15, verbose_name='Comisión')),
                ('status', models.CharField(choices=[('Activa', 'Activa'), ('Reagrupada', 'Reagrupada'), ('Cerrada', 'Cerrada'), ('Egresada', 'Egresada')], max_length=10)),
                ('campus', models.ForeignKey(on_delete=models.SET('Sede Eliminada'), to='fines.campus')),
            ],
            options={
                'verbose_name': 'Comisión',
                'verbose_name_plural': 'Comisiones',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_person', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Persona')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellido')),
                ('nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(blank=True, max_length=10, verbose_name='Género')),
                ('nacionalidad', models.CharField(blank=True, max_length=12, verbose_name='Nacionalidad')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('celular_1', models.IntegerField(verbose_name='Celular')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha inscripción')),
                ('domicilio', models.CharField(blank=True, max_length=100, verbose_name='Domicilio')),
                ('barrio', models.CharField(max_length=30, verbose_name='Localidad/Barrio')),
                ('celular_2', models.CharField(blank=True, max_length=10, verbose_name='Celular 2')),
                ('estudios', models.CharField(max_length=20, verbose_name='Estudios previos')),
                ('otros_estudios', models.CharField(max_length=255, verbose_name='Otros estudios')),
                ('materias_adeudadas', models.TextField(blank=True, verbose_name='Materias Adeudadas')),
                ('colegio', models.CharField(max_length=50, verbose_name='Colegio')),
                ('pais', models.CharField(max_length=12, verbose_name='País del colegio')),
                ('provincia', models.CharField(max_length=35, verbose_name='Provincia del colegio')),
                ('localidad', models.CharField(max_length=30, verbose_name='Ciudad del colegio')),
                ('turno_manana', models.BooleanField(default=False, verbose_name='Turno mañana')),
                ('turno_tarde', models.BooleanField(default=False, verbose_name='Turno tarde')),
                ('turno_noche', models.BooleanField(default=False, verbose_name='Turno noche')),
                ('sede', models.CharField(max_length=30, verbose_name='Sede de preferencia')),
                ('ex_alumno', models.BooleanField(default=False, verbose_name='Ex Alumno')),
                ('comision', models.ManyToManyField(to='fines.Comision')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Orientacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientacion', models.CharField(max_length=40, verbose_name='Orientación')),
                ('resolucion', models.CharField(max_length=10, verbose_name='N° Resolución')),
            ],
            options={
                'verbose_name': 'Orientación',
                'verbose_name_plural': 'Orientaciones',
            },
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.CharField(max_length=40, verbose_name='Asignatura')),
                ('horas', models.IntegerField(verbose_name='Horas Cátedra')),
                ('cuatrimestre', models.CharField(max_length=4, verbose_name='Cuatrimestre')),
                ('orientacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fines.orientacion', verbose_name='Orientación')),
            ],
            options={
                'verbose_name': 'Materias',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='Legajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libro', models.IntegerField(verbose_name='Libro')),
                ('folio', models.IntegerField(verbose_name='Folio')),
                ('dni_copia', models.BooleanField(verbose_name='DNI Copia')),
                ('p_nac_copia', models.BooleanField(verbose_name='P. Nac. Copia')),
                ('certificado', models.BooleanField(verbose_name='Certificado de estudios')),
                ('constancia', models.BooleanField(verbose_name='Constancia')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fines.estudiante', verbose_name='Estudiante')),
                ('orientacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fines.orientacion', verbose_name='Orientación')),
            ],
            options={
                'verbose_name': 'Legajo',
                'verbose_name_plural': 'Legajos',
            },
        ),
        migrations.AddField(
            model_name='comision',
            name='orientacion',
            field=models.ForeignKey(on_delete=models.SET('Orientación Eliminada'), to='fines.orientacion'),
        ),
    ]
