# Generated by Django 3.0.6 on 2020-05-28 18:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="belonging",
            name="owner",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
            preserve_default=False,
        ),
    ]