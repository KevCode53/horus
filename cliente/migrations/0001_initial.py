# Generated by Django 4.2.6 on 2023-10-23 22:41

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
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('nit', models.CharField(blank=True, default='C/F', max_length=25, null=True, verbose_name='NIT')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'client',
            },
        ),
    ]
