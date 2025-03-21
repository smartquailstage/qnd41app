# Generated by Django 4.2.16 on 2024-12-16 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbmshop', '0016_manualitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sbmproductmanual',
            name='color',
            field=models.CharField(blank=True, choices=[('rgb(133, 54, 140)', 'SBM-CRM+AI+I+D'), ('#0d0d0d', 'SBM-CRM'), ('#662d14', 'SBM-CRM+A'), ('#247832', 'SBM-CRM+I+D'), ('#7c7a21', 'SBM-CRM+A+I+D'), ('#283f75', 'SBM-CRM+AI'), ('#388e86', 'SBM-CRM+A+AI'), ('#251f25', 'SBM-CRM+A+AI+I+D')], db_index=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='SBMStaffItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceo_name', models.CharField(db_index=True, max_length=200)),
                ('ceo_lastname', models.CharField(db_index=True, max_length=200)),
                ('ceo_sector', models.CharField(choices=[('SmartBusinessMedia Community Manager', 'SmartBusinessMedia Community Manager'), ('Chief Officer of Technologies', 'Chief Officer of Technologies'), (' SmartBusinessMedia Project Manager', 'SmartBusinessMedia Project Manager'), ('Chief Officer SmartBusinessMedia', 'Chief Officer SmartBusinessMedia ')], db_index=True, max_length=200)),
                ('ceo_profile_img', models.ImageField(blank=True, upload_to='products/smartbusinessmedia/sbmstaff/%Y/%m/%d')),
                ('sbmproducts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffproducts', to='sbmshop.sbmproduct')),
            ],
        ),
    ]
