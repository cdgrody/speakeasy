# Generated by Django 4.1.6 on 2023-02-13 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_profile_primary_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profiles',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
