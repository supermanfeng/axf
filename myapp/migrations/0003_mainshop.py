# Generated by Django 2.0.2 on 2018-02-04 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contentthird'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=200)),
                ('trackid', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]
