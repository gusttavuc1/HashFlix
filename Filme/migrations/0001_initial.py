# Generated by Django 5.1 on 2024-08-18 14:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_filmes')),
                ('descricao', models.TextField(max_length=5000)),
                ('categoria', models.CharField(choices=[('analises', 'Análises'), ('apresentacao', 'Apresentação'), ('programacao', 'Programação')], max_length=30)),
                ('visualizacoes', models.IntegerField(default=0)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
