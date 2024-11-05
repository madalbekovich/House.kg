# Generated by Django 5.1.1 on 2024-11-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0017_delete_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='property',
            name='ceiling_height',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='Высота потолков'),
        ),
        migrations.AlterField(
            model_name='property',
            name='crossing',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Пересечение с'),
        ),
        migrations.AlterField(
            model_name='property',
            name='house_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='№ дома'),
        ),
        migrations.AlterField(
            model_name='typetranslation',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
