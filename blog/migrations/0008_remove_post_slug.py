# Generated by Django 5.0.6 on 2024-06-05 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_post_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="slug",
        ),
    ]