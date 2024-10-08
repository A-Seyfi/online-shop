# Generated by Django 5.0 on 2024-09-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0002_alter_orderdetail_color_alter_orderdetail_ram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='color',
            field=models.IntegerField(blank=True, max_length=50, null=True, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='ram',
            field=models.IntegerField(blank=True, max_length=50, null=True, verbose_name='رم'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='storage',
            field=models.IntegerField(blank=True, max_length=50, null=True, verbose_name='حافظه'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='warranty',
            field=models.IntegerField(blank=True, max_length=50, null=True, verbose_name='گارانتی'),
        ),
    ]
