# Generated by Django 4.0.5 on 2024-08-29 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('login', '0002_alter_user_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
