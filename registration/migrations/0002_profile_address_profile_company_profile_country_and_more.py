# Generated by Django 4.1.3 on 2024-10-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Job'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='LinkedIn Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter Profile'),
        ),
    ]
