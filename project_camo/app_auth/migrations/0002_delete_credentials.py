# Generated by Django 4.0.10 on 2024-05-13 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_user'),
        ('app_auth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Credentials',
        ),
    ]