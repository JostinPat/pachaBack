# Generated by Django 4.2.1 on 2023-06-03 15:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=150)),
                ('dni', models.CharField(default='72443245', max_length=10)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('img_path', models.CharField(max_length=500, null=True)),
                ('availability', models.PositiveSmallIntegerField(default=5)),
                ('password', models.CharField(default='1111111', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('max_student', models.PositiveSmallIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioColegio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=150)),
                ('dni', models.CharField(default='72443245', max_length=10)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('img_path', models.CharField(max_length=500, null=True)),
                ('availability', models.PositiveSmallIntegerField(default=5)),
                ('password', models.CharField(default='1111111', max_length=10)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.ciclo')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.aula')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.alumno')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.usuariocolegio')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('description', models.CharField(max_length=200, null=True)),
                ('availability', models.PositiveSmallIntegerField(default=5)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.ciclo')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.ciclo'),
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.DateField(default=datetime.date.today)),
                ('attendance', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.alumno')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.usuariocolegio')),
            ],
        ),
    ]
