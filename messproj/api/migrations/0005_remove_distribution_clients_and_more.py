# Generated by Django 4.0.3 on 2022-04-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_distribution_clients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribution',
            name='clients',
        ),
        migrations.AddField(
            model_name='distribution',
            name='clients_filter',
            field=models.JSONField(null=True),
        ),
    ]