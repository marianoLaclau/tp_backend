# Generated by Django 4.2.16 on 2024-12-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recursos',
            name='max_unidades',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
