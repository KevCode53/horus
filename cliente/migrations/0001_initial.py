# Generated by Django 4.2.6 on 2023-10-19 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('nit', models.CharField(max_length=25, verbose_name='NIT')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'client',
            },
        ),
    ]
