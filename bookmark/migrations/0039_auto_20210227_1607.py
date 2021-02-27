# Generated by Django 3.1.6 on 2021-02-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0038_auto_20210226_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='line',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='order',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
