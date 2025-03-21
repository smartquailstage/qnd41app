# Generated by Django 4.2.16 on 2024-12-21 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0024_sbmproduct_cloud_requirements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sbmstaffitem',
            name='sbmproducts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffproducts', to='sbmshop.sbmproduct'),
        ),
        migrations.AlterField(
            model_name='sbmtechnologiesitem',
            name='sbmproductstechno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technologies_products', to='sbmshop.sbmproduct'),
        ),
    ]
