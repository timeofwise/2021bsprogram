# Generated by Django 3.1.6 on 2021-02-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0026_auto_20210224_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_code', models.CharField(max_length=20, null=True)),
                ('part_name', models.CharField(max_length=30, null=True)),
                ('part_img', models.ImageField(default='photos/no_image.png', null=True, upload_to='static/img')),
            ],
        ),
    ]
