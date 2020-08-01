# Generated by Django 3.0.3 on 2020-08-01 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_activityperiod'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityperiod',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.User', verbose_name='User ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
