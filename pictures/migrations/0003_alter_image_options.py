# Generated by Django 4.0.4 on 2022-05-28 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_image_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created']},
        ),
    ]
