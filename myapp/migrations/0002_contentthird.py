# Generated by Django 2.0.2 on 2018-02-02 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentThird',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=200)),
                ('trackid', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
    ]