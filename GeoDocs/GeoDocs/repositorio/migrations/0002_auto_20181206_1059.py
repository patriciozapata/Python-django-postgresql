# Generated by Django 2.0.7 on 2018-12-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
