# Generated by Django 3.2.5 on 2021-07-08 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='title',
            new_name='header',
        ),
    ]
