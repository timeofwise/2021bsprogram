# Generated by Django 3.1.6 on 2021-02-20 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20210217_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='q3_2_1_future_interest_smart_erp',
            new_name='q3_21_fi_smart_erp',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='q3_2_2_future_interest_factory_automation',
            new_name='q3_22_fi_factory_automation',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='q3_2_3_future_interest_remote_support',
            new_name='q3_23_fi_remote_support',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='q3_2_4_future_interest_systematical_training',
            new_name='q3_24_fi_systematical_training',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='q3_2_5_future_interest_other',
            new_name='q3_25_fi_other',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='q3_2_5_other',
            new_name='q3_25_other',
        ),
    ]
