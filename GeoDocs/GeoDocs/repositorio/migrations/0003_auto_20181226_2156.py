# Generated by Django 2.0.7 on 2018-12-27 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0002_auto_20181206_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='autor',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='nombre',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='resumen',
            field=models.CharField(max_length=2000),
        ),
    ]
