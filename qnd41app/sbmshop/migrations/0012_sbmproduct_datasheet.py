# Generated by Django 4.2.16 on 2024-12-05 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0011_alter_sbmproduct_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='sbmproduct',
            name='datasheet',
            field=models.TextField(blank=True),
        ),
    ]
