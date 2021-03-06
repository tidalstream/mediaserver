# Generated by Django 2.2.8 on 2019-12-13 16:29

import django.db.models.deletion
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("unplugged", "0008_auto_20190715_1944"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("services_listing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identifier", models.CharField(max_length=100, unique=True)),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Metadata",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("priority", models.SmallIntegerField(default=20)),
                (
                    "last_update_status",
                    models.CharField(
                        choices=[
                            ("do-not-fetch", "Do not fetch"),
                            ("pending", "Pending"),
                            ("updating", "Updating"),
                            ("failed", "Failed"),
                            ("success", "Success"),
                        ],
                        db_index=True,
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("last_updated", models.DateTimeField(null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("identifier", models.CharField(max_length=255, unique=True)),
                ("populated", models.BooleanField(default=False)),
                ("title", models.CharField(max_length=300, null=True)),
                ("cover", models.URLField(max_length=1000, null=True)),
                (
                    "prefetch_related_denormalized",
                    jsonfield.fields.JSONField(blank=True, null=True),
                ),
                (
                    "rating",
                    models.DecimalField(decimal_places=2, max_digits=3, null=True),
                ),
                ("votes", models.IntegerField(null=True)),
                ("duration", models.IntegerField(null=True)),
                ("year", models.IntegerField(null=True)),
                ("plot", models.TextField(null=True)),
                ("synopsis", models.TextField(null=True)),
                (
                    "actors",
                    models.ManyToManyField(
                        related_name="actors", to="metadata_imdb.Person"
                    ),
                ),
                ("countries", models.ManyToManyField(to="metadata_imdb.Country")),
                (
                    "directors",
                    models.ManyToManyField(
                        related_name="directors", to="metadata_imdb.Person"
                    ),
                ),
                ("genres", models.ManyToManyField(to="metadata_imdb.Genre")),
                ("languages", models.ManyToManyField(to="metadata_imdb.Language")),
                (
                    "plugin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="metadata_metadata_imdb",
                        to="unplugged.Plugin",
                    ),
                ),
                (
                    "primary_language",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="primary_language",
                        to="metadata_imdb.Language",
                    ),
                ),
                (
                    "writers",
                    models.ManyToManyField(
                        related_name="writers", to="metadata_imdb.Person"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="AlternativeTitle",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                (
                    "metadata",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="metadata_imdb.Metadata",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MetadataResolutionLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("priority", models.SmallIntegerField(default=20)),
                (
                    "last_update_status",
                    models.CharField(
                        choices=[
                            ("do-not-fetch", "Do not fetch"),
                            ("pending", "Pending"),
                            ("updating", "Updating"),
                            ("failed", "Failed"),
                            ("success", "Success"),
                        ],
                        db_index=True,
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("last_updated", models.DateTimeField(null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=255)),
                ("search_resolve", models.CharField(max_length=30)),
                (
                    "listingitems",
                    models.ManyToManyField(
                        related_name="resolution_metadata_imdb",
                        to="services_listing.ListingItem",
                    ),
                ),
                (
                    "metadata",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="metadata_imdb.Metadata",
                    ),
                ),
                (
                    "plugin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resolution_metadata_imdb",
                        to="unplugged.Plugin",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("name", "search_resolve")},
            },
        ),
        migrations.CreateModel(
            name="ListingItemRelation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "listingitem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="metadata_imdb",
                        to="services_listing.ListingItem",
                    ),
                ),
                (
                    "metadata",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="metadata_imdb.Metadata",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="metadata_imdb",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("listingitem", "metadata", "user")},
            },
        ),
    ]
