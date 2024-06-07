# Generated by Django 5.0.6 on 2024-06-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("author", models.CharField(max_length=80)),
                ("body", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]