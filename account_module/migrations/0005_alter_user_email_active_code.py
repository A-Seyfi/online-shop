# Generated by Django 5.0 on 2024-09-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_active_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='کد فعالسازی ایمیل'),
        ),
    ]
