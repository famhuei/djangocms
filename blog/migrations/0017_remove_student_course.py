# Generated by Django 5.0.6 on 2024-06-07 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_course_students"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="course",
        ),
    ]
