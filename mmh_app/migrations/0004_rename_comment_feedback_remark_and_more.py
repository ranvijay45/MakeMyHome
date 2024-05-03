# Generated by Django 5.0.4 on 2024-04-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmh_app', '0003_homeowner_user_manager_user_servicerequest_architech_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='comment',
            new_name='remark',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='homeowner',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='rating',
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='Annonymous', max_length=50),
        ),
    ]
