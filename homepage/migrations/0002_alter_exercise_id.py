# Generated by Django 4.0.1 on 2022-01-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
