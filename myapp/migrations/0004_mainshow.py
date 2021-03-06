# Generated by Django 2.0.2 on 2018-02-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_mainshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=200)),
                ('trackid', models.CharField(max_length=32)),
                ('categoryid', models.CharField(max_length=32)),
                ('brandname', models.CharField(max_length=100)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=32)),
                ('productid1', models.CharField(max_length=32)),
                ('longname1', models.CharField(max_length=200)),
                ('price1', models.CharField(max_length=100)),
                ('marketprice1', models.CharField(max_length=100)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=32)),
                ('productid2', models.CharField(max_length=32)),
                ('longname2', models.CharField(max_length=200)),
                ('price2', models.CharField(max_length=100)),
                ('marketprice2', models.CharField(max_length=100)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=32)),
                ('productid3', models.CharField(max_length=32)),
                ('longname3', models.CharField(max_length=200)),
                ('price3', models.CharField(max_length=100)),
                ('marketprice3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'axf_mainshop',
            },
        ),
    ]
