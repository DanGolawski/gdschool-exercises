# Generated by Django 4.0.1 on 2022-02-26 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_remove_chapter_book_remove_topic_book_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='book_id',
            new_name='book',
        ),
    ]
