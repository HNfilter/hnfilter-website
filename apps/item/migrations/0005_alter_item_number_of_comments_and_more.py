# Generated by Django 4.1.7 on 2023-03-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_number_of_comments_alter_item_number_of_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='number_of_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='number_of_votes',
            field=models.IntegerField(default=0),
        ),
    ]