# Generated by Django 4.0.3 on 2022-04-01 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_post_f1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posts',
            new_name='cover',
        ),
    ]
