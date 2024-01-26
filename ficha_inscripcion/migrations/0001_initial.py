# Generated by Django 5.0.1 on 2024-01-21 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

  initial = True

  dependencies = [
  ('socios', '0003_alter_socio_options'),
  ('tipo_deporte', '0001_initial'),
  ]

  operations = [
  migrations.CreateModel(
    name='FichaInscripcion',
    fields=[
    ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    ('fecha_inscripcion', models.DateField(auto_now_add=True)),
    ('monto_inscripcion', models.DecimalField(decimal_places=2, max_digits=6)),
    ('estado', models.CharField(default='A', max_length=1)),
    ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socios.socio')),
    ('tipo_deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_deporte.tipodeporte')),
    ],
    options={
    'verbose_name': 'Ficha de Inscripcion',
    'verbose_name_plural': 'Fichas de Inscripciones',
    'ordering': ['id'],
    },
  ),
  ]
