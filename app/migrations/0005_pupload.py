# Generated by Django 4.1.3 on 2022-11-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_file_bupload_fileb_rename_file_fupload_filef'),
    ]

    operations = [
        migrations.CreateModel(
            name='PUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filep', models.ImageField(upload_to='images/')),
            ],
        ),
    ]