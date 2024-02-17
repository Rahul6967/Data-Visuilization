# Generated by Django 4.2.9 on 2024-02-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="blackcoffer",
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
                ("end_year", models.TextField(max_length=4)),
                ("intensity", models.TextField(max_length=3)),
                ("sector", models.TextField(max_length=30)),
                ("topic", models.TextField(max_length=20)),
                ("insight", models.TextField(max_length=150)),
                ("url", models.TextField(max_length=500)),
                ("region", models.TextField(max_length=50)),
                ("start_year", models.TextField(max_length=4)),
                ("impact", models.TextField(max_length=50)),
                ("added", models.TextField(max_length=40)),
                ("published", models.TextField(max_length=40)),
                ("country", models.TextField(max_length=40)),
                ("relevance", models.TextField(max_length=3)),
                ("pestle", models.TextField(max_length=20)),
                ("source", models.TextField(max_length=200)),
                ("title", models.TextField(max_length=500)),
                ("likelihood", models.TextField(max_length=3)),
            ],
        ),
    ]