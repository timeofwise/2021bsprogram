# Generated by Django 3.1.6 on 2021-02-03 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100)),
                ('model_no', models.CharField(max_length=20)),
                ('model_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookmark.machine')),
            ],
        ),
    ]

'''
                ('col_1', models.IntegerField(default=1)),
                ('col_2', models.IntegerField(default=1)),
                ('col_3', models.IntegerField(default=1)),
                ('col_4', models.IntegerField(default=1)),
                ('col_5', models.IntegerField(default=1)),
                ('col_6', models.IntegerField(default=1)),
                ('col_7', models.IntegerField(default=1)),
                ('col_8', models.IntegerField(default=1)),
                ('col_9', models.IntegerField(default=1)),
                ('col_10', models.IntegerField(default=1)),
                ('col_11', models.IntegerField(default=1)),
                ('col_12', models.IntegerField(default=1)),
                ('col_13', models.IntegerField(default=1)),
                ('col_14', models.IntegerField(default=1)),
                ('col_15', models.IntegerField(default=1)),
                ('col_16', models.IntegerField(default=1)),
                ('col_17', models.IntegerField(default=1)),
                ('col_18', models.IntegerField(default=1)),
                ('col_19', models.IntegerField(default=1)),
                ('col_20', models.IntegerField(default=1)),
                ('col_21', models.IntegerField(default=1)),
                ('col_22', models.IntegerField(default=1)),
                ('col_23', models.IntegerField(default=1)),
                ('col_24', models.IntegerField(default=1)),
                ('col_25', models.IntegerField(default=1)),
                ('col_26', models.IntegerField(default=1)),
                ('col_27', models.IntegerField(default=1)),
                ('col_28', models.IntegerField(default=1)),
                ('col_29', models.IntegerField(default=1)),
'''