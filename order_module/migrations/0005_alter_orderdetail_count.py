# Generated by Django 5.0 on 2024-09-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0004_alter_orderdetail_color_alter_orderdetail_ram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='تعداد'),
        ),
    ]
