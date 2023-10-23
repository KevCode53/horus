# Generated by Django 4.2.6 on 2023-10-23 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/image')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Imagen')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.category')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'product',
            },
        ),
    ]
