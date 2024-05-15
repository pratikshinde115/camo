# Generated by Django 5.0.4 on 2024-05-09 04:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_auth", "0002_alter_credentials_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="credentials",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="credentials",
            name="password",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="credentials",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
