# Generated by Django 4.2.1 on 2023-06-02 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("control", "0009_request"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="course",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="control.course",
            ),
        ),
    ]