# Generated by Django 3.0.3 on 2020-08-01 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200801_1207'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]