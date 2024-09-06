# Generated by Django 4.0.5 on 2024-08-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('login', '0003_remove_user_role_remove_user_groups_user_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.group'),
        ),
    ]
