# Generated by Django 4.2.1 on 2023-05-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acms', '0004_alter_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='old_photo',
            field=models.TextField(default='', verbose_name='old_photo'),
        ),
    ]
