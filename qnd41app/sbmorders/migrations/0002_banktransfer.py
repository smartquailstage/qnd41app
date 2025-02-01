# Generated by Django 4.2.16 on 2024-12-05 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbmorders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(choices=[('banco_pichincha', 'Banco de Pichincha'), ('produbanco', 'Banco Produbanco'), ('banco_internacional', 'Banco Internacional'), ('banco_guayaquil', 'Banco de Guayaquil')], max_length=20)),
                ('transfer_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.CharField(max_length=255)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sbmorders.order')),
            ],
        ),
    ]
