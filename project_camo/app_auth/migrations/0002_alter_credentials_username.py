# Generated by Django 5.0.4 on 2024-05-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="credentials",
            name="username",
            field=models.CharField(default="username", max_length=50, unique=True),
        ),
    ]