# Generated by Django 5.0.6 on 2024-06-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trainer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("course", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=40)),
                (
                    "departament",
                    models.CharField(
                        choices=[("B", "Backend"), ("F", "Frontend"), ("N", "Network")],
                        max_length=40,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]