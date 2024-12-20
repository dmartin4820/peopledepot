# Generated by Django 4.2.11 on 2024-10-29 03:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0028_alter_userpermission_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectSdgXref",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "ended_on",
                    models.DateField(blank=True, null=True, verbose_name="Ended on"),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.project"
                    ),
                ),
                (
                    "sdg_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.sdg"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="project",
            name="sdgs",
            field=models.ManyToManyField(
                blank=True,
                related_name="projects",
                through="core.ProjectSdgXref",
                to="core.sdg",
            ),
        ),
    ]
