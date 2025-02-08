# Generated by Django 4.2.18 on 2025-02-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCampaignSnippet',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('mailing.emailcampaign',),
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='expire_at',
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='expired',
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='first_published_at',
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='go_live_at',
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='has_unpublished_changes',
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='last_published_at',
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='latest_revision',
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='live',
        ),
        migrations.RemoveField(
            model_name='emailcampaign',
            name='live_revision',
        ),
        migrations.AlterField(
            model_name='emailcampaign',
            name='send_date',
            field=models.DateTimeField(),
        ),
    ]
