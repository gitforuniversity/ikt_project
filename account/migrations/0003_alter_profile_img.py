# Generated by Django 4.2.1 on 2023-05-20 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='profile/img/default.png', upload_to='profile/img'),
        ),
    ]
