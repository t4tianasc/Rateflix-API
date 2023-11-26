# Generated by Django 4.2.7 on 2023-11-25 12:45

from django.db import migrations


def update_existing_records(apps, schema_editor):
    MyModel = apps.get_model('movies', 'Movie')
    MyModel.objects.update(thumbnail='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzfKpE7moB9tkOdWtUSe18WWPr8UxxFOm4BA&usqp=CAU')


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_thumbnail'),
    ]

    operations = [
        migrations.RunPython(update_existing_records),
    ]
