# Generated by Django 4.2.1 on 2023-06-02 20:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("control", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enrollment",
            name="teacher",
        ),
    ]