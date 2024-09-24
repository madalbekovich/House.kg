# Generated by Django 5.1.1 on 2024-09-24 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_remove_contactinfo_user_contactinfo_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='contact_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contact_info_property', to='house.contactinfo', verbose_name='Контактная информация'),
            preserve_default=False,
        ),
    ]
