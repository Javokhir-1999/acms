# Generated by Django 4.2.1 on 2023-05-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acms', '0002_person_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(default=False, editable=False, null=True, upload_to='media/'),
        ),
    ]
