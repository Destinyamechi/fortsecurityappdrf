# Generated by Django 4.2.4 on 2023-09-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_remove_mode_tier_tier_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tier',
            name='number_of_organizations',
        ),
        migrations.AddField(
            model_name='tier',
            name='bio',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]