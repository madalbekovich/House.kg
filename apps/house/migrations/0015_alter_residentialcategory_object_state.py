# Generated by Django 5.1.1 on 2024-11-01 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0014_rename_building_residentialcategory_material_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residentialcategory',
            name='object_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='house.buildingstate', verbose_name='Состояние обьекта'),
        ),
    ]
