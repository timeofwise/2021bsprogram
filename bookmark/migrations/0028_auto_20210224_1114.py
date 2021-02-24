# Generated by Django 3.1.6 on 2021-02-24 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0027_consumed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='part1_code',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='part1_img',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='part1_name',
        ),
        migrations.AddField(
            model_name='machine',
            name='part1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookmark.consumed', to_field='part_code'),
        ),
        migrations.AlterField(
            model_name='consumed',
            name='part_code',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]