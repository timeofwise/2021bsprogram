# Generated by Django 3.1.6 on 2021-04-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodetest', '0002_auto_20210401_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr_info',
            name='ver_vision',
            field=models.CharField(max_length=20, null=True),
        ),
    ]