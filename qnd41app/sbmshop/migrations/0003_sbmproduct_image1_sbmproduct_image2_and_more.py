# Generated by Django 4.2.16 on 2024-12-04 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0002_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='sbmproduct',
            name='image1',
            field=models.ImageField(blank=True, upload_to='products/smartbusinessmedia/scren1/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='sbmproduct',
            name='image2',
            field=models.ImageField(blank=True, upload_to='products/smartbusinessmedia/scren2/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='sbmproduct',
            name='image3',
            field=models.ImageField(blank=True, upload_to='products/smartbusinessmedia/scren3/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='sbmproduct',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/smartbusinessmedia/bannering/%Y/%m/%d'),
        ),
    ]
