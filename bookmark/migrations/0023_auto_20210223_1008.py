# Generated by Django 3.1.6 on 2021-02-23 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0022_auto_20210221_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['-updated']},
        ),
    ]
