# Generated by Django 3.1.6 on 2021-02-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0023_auto_20210223_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='visibility',
            field=models.IntegerField(default=1, null=True),
        ),
    ]