# Generated by Django 4.1.3 on 2022-11-12 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_fupload_rename_upload_bupload_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bupload',
            old_name='file',
            new_name='fileb',
        ),
        migrations.RenameField(
            model_name='fupload',
            old_name='file',
            new_name='filef',
        ),
    ]
