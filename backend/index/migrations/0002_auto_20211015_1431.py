# Generated by Django 3.2.8 on 2021-10-15 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deceased',
            name='condolences',
        ),
        migrations.RemoveField(
            model_name='deceased',
            name='imageGallery',
        ),
        migrations.RemoveField(
            model_name='deceased',
            name='no_condolence',
        ),
    ]
