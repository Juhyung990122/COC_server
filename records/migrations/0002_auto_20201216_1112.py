# Generated by Django 3.1.4 on 2020-12-16 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='reader',
            field=models.ForeignKey(db_column='users_id', on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
