# Generated by Django 4.2.16 on 2024-12-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0019_alter_sbmstaffitem_sbmproducts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sbmproduct',
            name='item1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sbmproduct',
            name='item2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sbmproduct',
            name='item3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sbmproduct',
            name='item4',
            field=models.TextField(blank=True, null=True),
        ),
    ]
