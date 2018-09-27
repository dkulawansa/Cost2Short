# Generated by Django 2.0.4 on 2018-09-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=5)),
                ('curency', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=255)),
                ('con', models.IntegerField()),
                ('isin', models.CharField(max_length=255)),
                ('rebate_rate', models.FloatField()),
                ('fee_rate', models.FloatField()),
                ('amount', models.CharField(max_length=255)),
            ],
        ),
    ]