# Generated by Django 4.0.1 on 2022-02-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_exercise_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]