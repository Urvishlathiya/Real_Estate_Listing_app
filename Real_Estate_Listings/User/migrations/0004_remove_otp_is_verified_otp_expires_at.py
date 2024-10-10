# Generated by Django 5.1.1 on 2024-10-07 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0003_otp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="otp",
            name="is_verified",
        ),
        migrations.AddField(
            model_name="otp",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 10, 7, 10, 2, 20, 421657, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]