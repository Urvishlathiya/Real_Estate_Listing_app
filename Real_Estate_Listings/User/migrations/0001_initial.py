# Generated by Django 5.1.1 on 2024-09-11 09:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("username", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=15)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("buyer", "Buyer"),
                            ("seller", "Seller"),
                            ("agent", "Agent"),
                        ],
                        default="buyer",
                        max_length=10,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
