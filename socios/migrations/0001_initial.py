# Generated by Django 5.0.1 on 2024-01-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Socios',
      fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('nombres', models.CharField(max_length=50)),
        ('apellidos', models.CharField(max_length=50)),
        ('dni', models.CharField(max_length=8)),
        ('estado', models.CharField(default='A', max_length=1)),
      ],
      options={
        'verbose_name': 'Socio',
        'verbose_name_plural': 'Socios',
        'ordering': ['nombres'],
      },
    ),
  ]
