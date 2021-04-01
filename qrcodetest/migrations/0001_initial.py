# Generated by Django 3.1.6 on 2021-03-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='qr_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=10, null=True)),
                ('model_no', models.CharField(max_length=10, null=True, unique=True)),
                ('ver_sw', models.CharField(max_length=30, null=True)),
                ('ver_mmi', models.CharField(max_length=20, null=True)),
                ('ver_rt', models.CharField(max_length=20, null=True)),
                ('ver_opti', models.CharField(max_length=20, null=True)),
                ('ver_it', models.CharField(max_length=20, null=True)),
                ('option_1', models.BooleanField(default=False, null=True)),
                ('option_2', models.BooleanField(default=False, null=True)),
                ('option_3', models.BooleanField(default=False, null=True)),
                ('option_4', models.BooleanField(default=False, null=True)),
                ('option_5', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]