# Generated by Django 5.0.6 on 2024-06-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0020_remove_student_institue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]