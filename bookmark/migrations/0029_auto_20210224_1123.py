# Generated by Django 3.1.6 on 2021-02-24 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0028_auto_20210224_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='part2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='part2', to='bookmark.consumed', to_field='part_code'),
        ),
        migrations.AddField(
            model_name='machine',
            name='part2_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='part1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='part1', to='bookmark.consumed', to_field='part_code'),
        ),
    ]
