# Generated by Django 5.1.3 on 2025-05-12 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservations",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("guest_count", models.IntegerField()),
                ("resevation_time", models.DateTimeField(auto_now=True)),
                ("Comments", models.CharField(max_length=1000)),
            ],
        ),
    ]
