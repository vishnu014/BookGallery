# Generated by Django 4.0.1 on 2022-02-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districts',
            name='district_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
