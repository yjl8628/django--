# Generated by Django 4.1 on 2022-08-12 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0002_posts_delete_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
