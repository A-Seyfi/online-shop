# Generated by Django 3.2.12 on 2022-04-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0005_alter_slider_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteBanners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('position', models.CharField(choices=[('product_list', 'لیست محصولات'), ('product_detail', 'جزییات محصول')], max_length=200)),
            ],
        ),
    ]
