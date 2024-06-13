# Generated by Django 5.0.6 on 2024-06-09 06:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Gallery", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="user_id",
            field=models.ForeignKey(
                db_column="user_id",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="love",
            name="user_id",
            field=models.ForeignKey(
                db_column="user_id",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="picture",
            name="user_id",
            field=models.ForeignKey(
                db_column="user_id",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="love",
            name="picture_id",
            field=models.ForeignKey(
                db_column="picture_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="Gallery.picture",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="picture_id",
            field=models.ForeignKey(
                db_column="picture_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="Gallery.picture",
            ),
        ),
    ]