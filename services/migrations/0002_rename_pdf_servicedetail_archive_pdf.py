# Generated by Django 4.1.3 on 2024-10-12 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicedetail',
            old_name='pdf',
            new_name='archive_pdf',
        ),
    ]