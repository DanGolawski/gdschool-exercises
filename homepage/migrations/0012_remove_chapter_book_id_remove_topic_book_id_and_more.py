# Generated by Django 4.0.1 on 2022-02-26 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_rename_book_chapter_book_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='book_id',
        ),
        migrations.AddField(
            model_name='chapter',
            name='book',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='book',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
