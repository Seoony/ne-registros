# Generated by Django 5.0.1 on 2024-01-21 19:42

from django.db import migrations


class Migration(migrations.Migration):

  dependencies = [
    ('socios', '0002_rename_socios_socio'),
  ]

  operations = [
    migrations.AlterModelOptions(
      name='socio',
      options={'ordering': ['id'], 'verbose_name': 'Socio', 'verbose_name_plural': 'Socios'},
    ),
  ]
