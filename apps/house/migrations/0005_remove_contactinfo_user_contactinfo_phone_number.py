# Generated by Django 5.1.1 on 2024-09-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_alter_contactinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='phone_number',
            field=models.CharField(default=1, max_length=16, verbose_name='Номер телефона пользователя'),
            preserve_default=False,
        ),
    ]
