# Generated by Django 4.2.6 on 2023-11-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_product_show_alert_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('servicios', 'Servicios')], max_length=255, verbose_name='Name'),
        ),
    ]
