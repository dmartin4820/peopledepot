# Generated by Django 4.2.16 on 2025-03-27 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_projectstatus_project_current_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionHistory',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_permission_created_by', to=settings.AUTH_USER_MODEL)),
                ('permission_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.permissiontype')),
                ('practice_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.practicearea')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_permission_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
