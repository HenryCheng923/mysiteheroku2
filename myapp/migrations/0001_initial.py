# Generated by Django 2.2.4 on 2019-10-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('stockid', models.PositiveIntegerField(db_column='StockID', primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(blank=True, db_column='Abbreviation', max_length=10, null=True, unique=True)),
                ('url', models.CharField(blank=True, db_column='URL', max_length=128, null=True, unique=True)),
                ('employees', models.PositiveIntegerField(blank=True, db_column='Employees', null=True)),
                ('capital', models.BigIntegerField(blank=True, db_column='Capital', null=True)),
                ('industryname', models.CharField(db_column='IndustryName', max_length=16)),
                ('listeddate', models.CharField(blank=True, db_column='ListedDate', max_length=45, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
    ]