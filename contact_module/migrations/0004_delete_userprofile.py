# Generated by Django 5.1.1 on 2024-10-10 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0003_alter_contactus_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
