# Generated by Django 3.2.8 on 2022-06-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0003_alter_albummodel_album_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='album_logo',
            field=models.ImageField(blank=True, null=True, upload_to='album_logos/'),
        ),
    ]
