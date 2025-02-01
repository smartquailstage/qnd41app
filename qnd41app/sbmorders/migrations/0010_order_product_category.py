# Generated by Django 4.2.16 on 2024-12-08 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0013_sbmproduct_terms_conditions'),
        ('sbmorders', '0009_orderitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category_items', to='sbmshop.category'),
        ),
    ]
