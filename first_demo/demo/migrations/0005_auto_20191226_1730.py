# Generated by Django 2.2.9 on 2019-12-26 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_book_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='descrtiption',
            new_name='description',
        ),
    ]
