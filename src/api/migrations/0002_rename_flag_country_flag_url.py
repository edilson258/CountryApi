# Generated by Django 4.0.4 on 2022-06-03 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='flag',
            new_name='flag_url',
        ),
    ]