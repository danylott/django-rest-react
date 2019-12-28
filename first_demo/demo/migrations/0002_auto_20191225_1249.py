# Generated by Django 3.0.1 on 2019-12-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(choices=[('HB', 'Hobbit'), ('LOTR', 'Lord of the ring')], max_length=50, unique=True),
        ),
    ]