# Generated by Django 4.0.2 on 2022-04-06 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_rename_owner_trans_data_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trans_data',
            old_name='user',
            new_name='owner',
        ),
    ]
