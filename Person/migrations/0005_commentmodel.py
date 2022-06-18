# Generated by Django 3.2.8 on 2022-06-17 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0004_rename_firstname_personmodel_firstname'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(blank=True, null=True, verbose_name='Yorum')),
                ('comment_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Person.personmodel', verbose_name='Yorum Kullanıcısı')),
            ],
        ),
    ]
