# Generated by Django 4.2.4 on 2023-09-15 16:35

from django.db import migrations, models
import django.db.models.deletion
import producto.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la categoria Principal', max_length=30)),
                ('imagen', models.ImageField(blank=True, default='imagen/productos/404.png', help_text='Imagen de la categoria', null=True, upload_to=producto.models.nombreImagen)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(help_text='Ciudad del proveedor', max_length=30)),
                ('nombre_completo', models.CharField(help_text='Nombre Proveedor', max_length=60)),
                ('nit', models.CharField(help_text='Numero de identifiacion tributaria + digito de verificación adicional o numero de cedula', max_length=15)),
                ('correo_electronico', models.EmailField(help_text='Correo electronico del proveedor', max_length=200, unique=True)),
                ('telefono', models.CharField(help_text='Numero de telefono con identificador de pais', max_length=13)),
                ('direccion', models.CharField(help_text='Dirección del proveedor Cll or Cr + ##-##', max_length=50)),
            ],
            options={
                'db_table': 'proveedor',
            },
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la subcategoria Segundario', max_length=20)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.categoria')),
            ],
            options={
                'db_table': 'subcategoria',
            },
        ),
    ]
