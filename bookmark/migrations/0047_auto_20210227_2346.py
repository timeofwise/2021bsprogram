# Generated by Django 3.1.6 on 2021-02-27 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0046_auto_20210227_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='desc',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
