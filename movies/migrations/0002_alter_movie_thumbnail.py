# Generated by Django 4.2.7 on 2023-11-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzfKpE7moB9tkOdWtUSe18WWPr8UxxFOm4BA&usqp=CAU'),
        ),
    ]