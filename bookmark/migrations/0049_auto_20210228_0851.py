# Generated by Django 3.1.6 on 2021-02-28 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0048_report_mini_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='img2',
            field=models.ImageField(default='photos/no_image.png', null=True, upload_to='static/img/report'),
        ),
        migrations.AddField(
            model_name='report',
            name='img3',
            field=models.ImageField(default='photos/no_image.png', null=True, upload_to='static/img/report'),
        ),
    ]