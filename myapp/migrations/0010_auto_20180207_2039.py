# Generated by Django 2.0.2 on 2018-02-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20180206_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='o_create_time',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
