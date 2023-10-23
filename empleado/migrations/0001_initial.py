# Generated by Django 4.2.6 on 2023-10-23 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('start_at_work', models.DateField(blank=True, null=True, verbose_name='Start at Work')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salary')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'employee',
            },
        ),
    ]
