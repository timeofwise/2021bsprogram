# Generated by Django 3.1.6 on 2021-02-20 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20210220_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='q3_1_main_concern',
            field=models.CharField(default='-', max_length=80, null=True),
        ),
    ]
