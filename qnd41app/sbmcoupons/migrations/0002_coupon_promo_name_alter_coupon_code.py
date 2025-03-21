# Generated by Django 4.2.16 on 2024-12-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbmcoupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='promo_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=50, unique=True, verbose_name='Write the promotional Code'),
        ),
    ]
