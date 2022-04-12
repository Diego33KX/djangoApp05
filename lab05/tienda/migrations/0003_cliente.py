# Generated by Django 4.0.4 on 2022-04-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('fecha_nacimiento', models.DateField(verbose_name='date of birth')),
                ('fecha_publicacion', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
