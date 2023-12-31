# Generated by Django 4.2.6 on 2023-10-27 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compra', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0002_initial'),
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='payment',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='buydetail',
            name='buy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.buy'),
        ),
        migrations.AddField(
            model_name='buydetail',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='buydetail',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.product'),
        ),
        migrations.AddField(
            model_name='buydetail',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='buy',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='buy',
            name='provider_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.providers'),
        ),
        migrations.AddField(
            model_name='buy',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
    ]
