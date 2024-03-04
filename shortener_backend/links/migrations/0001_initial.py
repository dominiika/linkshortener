# Generated by Django 5.0.2 on 2024-03-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
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
                ("original_url", models.URLField(max_length=255)),
                (
                    "shortened_url",
                    models.URLField(default="", max_length=255, unique=True),
                ),
                (
                    "shortened_url_path",
                    models.CharField(default="", max_length=255, unique=True),
                ),
                ("display_number", models.IntegerField(default=0)),
                ("user_metadata", models.JSONField(default=dict)),
            ],
        ),
    ]