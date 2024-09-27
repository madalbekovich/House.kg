# Generated by Django 5.1.1 on 2024-09-27 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_property_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='documents',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_property', to='house.documents', verbose_name='Правоустанавливающие документы'),
        ),
        migrations.AlterField(
            model_name='property',
            name='miscellaneous',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miscellaneous_property', to='house.miscellaneous', verbose_name='Разное'),
        ),
        migrations.AlterField(
            model_name='property',
            name='security',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='security_property', to='house.security', verbose_name='Безопасность'),
        ),
    ]
