# Generated by Django 4.2.16 on 2024-12-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbmorders', '0004_remove_banktransfer_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banktransfer',
            name='bank_id',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Bank Transaction ID'),
        ),
    ]
