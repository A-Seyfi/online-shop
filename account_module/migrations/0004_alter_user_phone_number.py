# Generated by Django 5.0 on 2024-09-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_remove_user_about_user_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره تلفن'),
        ),
    ]
