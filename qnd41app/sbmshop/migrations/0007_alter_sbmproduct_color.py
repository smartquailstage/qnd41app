# Generated by Django 4.2.16 on 2024-12-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0006_alter_sbmproduct_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sbmproduct',
            name='color',
            field=models.CharField(blank=True, choices=[('rgb(133, 54, 140)', 'SBM-CRM+AI+I+D'), ('#5a5a59', 'SBM-CRM'), ('#662d14', 'SBM-CRM+A'), ('#377933', 'SBM-CRM+A+I+D'), ('#283f75', 'SBM-CRM+AI'), ('#388e86', 'SBM-CRM+A+AI'), ('#251f25', 'SBM-CRM+A+AI+I+D')], db_index=True, max_length=200, null=True),
        ),
    ]
