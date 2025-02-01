# Generated by Django 4.2.16 on 2024-12-19 04:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0023_sbmproduct_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='sbmproduct',
            name='cloud_requirements',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='sbmproduct',
            name='cloud_technologies',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sbmproduct',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
