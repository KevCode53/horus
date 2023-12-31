# Generated by Django 4.2.6 on 2023-10-27 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='providers',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
    ]
