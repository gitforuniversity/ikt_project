# Generated by Django 4.2.1 on 2023-05-21 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='base',
            old_name='update_datt',
            new_name='update_date',
        ),
    ]