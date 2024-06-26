# Generated by Django 5.0.4 on 2024-04-28 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmh_app', '0002_alter_architect_specilization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeowner',
            name='user',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='architech',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mmh_app.architect'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='contractor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mmh_app.contractor'),
        ),
    ]
