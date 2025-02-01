# Generated by Django 4.2.16 on 2024-12-08 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0013_sbmproduct_terms_conditions'),
        ('sbmorders', '0008_alter_banktransfer_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sbmshop.category'),
        ),
    ]
