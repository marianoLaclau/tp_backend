# Generated by Django 5.1.1 on 2024-10-19 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('personal_asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.personaladmin')),
            ],
        ),
    ]
