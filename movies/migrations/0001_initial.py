# Generated by Django 4.1.7 on 2023-02-17 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(default=None, max_length=10, null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("PG", "Pg"),
                            ("PG-13", "Pg13"),
                            ("R", "R"),
                            ("NC-17", "Nc17"),
                            ("G", "Default"),
                        ],
                        default="G",
                        max_length=20,
                    ),
                ),
                ("synopsis", models.TextField(default=None, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]