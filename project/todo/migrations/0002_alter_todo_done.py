# Generated by Django 4.2.3 on 2023-07-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]